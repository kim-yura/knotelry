<template>
    <div class="projects-page">
        <div class="projects-page-left">
            <form class="projects-search-container" @submit.prevent="submit">
                <p class="header">Search Options</p>
                <div>
                    <label>Search by Title or Description</label>
                    <input
                        type="text"
                        placeholder="Search for anything..."
                        v-model="searchParam"
                    />
                </div>
                <div>
                    <label>Filter by Status</label>
                    <select name="status" id="status" v-model="searchStatus">
                        <option value="null" selected disabled hidden>—</option>
                        <option value="queued">Queued</option>
                        <option value="inProgress">In Progress</option>
                        <option value="finished">Finished</option>
                        <option value="timeout">In Time Out</option>
                    </select>
                </div>
                <div>
                    <label>Filter by Craft Type</label>
                    <div class="craft-options">
                        <button
                            type="button"
                            v-bind:class="{ selected: searchSpinning }"
                            @click.prevent="
                                this.searchSpinning = !this.searchSpinning
                            "
                        >
                            Spinning
                        </button>
                        <button
                            type="button"
                            v-bind:class="{ selected: searchKnitting }"
                            @click.prevent="
                                this.searchKnitting = !this.searchKnitting
                            "
                        >
                            Knitting
                        </button>
                        <button
                            type="button"
                            v-bind:class="{ selected: searchSewing }"
                            @click.prevent="
                                this.searchSewing = !this.searchSewing
                            "
                        >
                            Sewing
                        </button>
                    </div>
                </div>
                <div>
                    <button id="submit-search">Search!</button>
                    <p id="reset-search" @click="reset">
                        Reset Projects Search
                    </p>
                </div>
            </form>
        </div>
        <div class="projects-body">
            <div class="projects-header">
                <h2>{{ $store.state.selectedUser?.username }}'s Projects</h2>
                <h4
                    @click="createProject"
                    v-if="$store.state.sessionUser?.id == $route.params.id"
                >
                    <i class="fas fa-plus-circle" />Add New Project
                </h4>
            </div>
            <div
                class="projects-gallery"
                v-if="$store.state.usersProjects?.length"
            >
                <div
                    class="project-card"
                    v-for="project in $store.state.usersProjects"
                    :key="project.id"
                >
                    <img
                        v-if="project.projectImages.length"
                        @click="redirectDetail(project.id)"
                        class="card-image"
                        :src="project.projectImages[0].imageURL"
                        alt="User uploaded image of project"
                    />
                    <img
                        v-else
                        @click="redirectDetail(project.id)"
                        class="card-image"
                        src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                        alt="No image found"
                    />
                    <p @click="redirectDetail(project.id)" class="card-header">
                        {{ project.title }}
                    </p>
                </div>
            </div>
            <div class="projects-gallery-no-results" v-else>
                <h4>No results!</h4>
                <p>
                    Maybe try broadening your search or
                    <span id="create-link" @click="createProject"
                        >adding a new project?</span
                    >
                </p>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "Projects",
    mounted() {
        this.$store.commit("clearSelectedUser");
        const data = loadUser(this.$route.params.id).then((data) => {
            if (data) {
                this.$store.commit("setSelectedUser", data);
            } else {
                this.$router.push("/404");
            }
        });
        const projectsData = loadUsersProjects(this.$route.params.id).then(
            (projectsData) => {
                if (projectsData) {
                    this.$store.commit("setUsersProjects", projectsData);
                    if (this.$route.params.craftParam) {
                        if (this.$route.params.craftParam == "spinning") {
                            this.searchSpinning = true;
                        } else if (
                            this.$route.params.craftParam == "knitting"
                        ) {
                            this.searchKnitting = true;
                        } else if (this.$route.params.craftParam == "sewing") {
                            this.searchSewing = true;
                        }

                        const temp = new Set();
                        if (this.searchSpinning) {
                            Object.values(projectsData)[0].forEach(
                                (project) => {
                                    if (
                                        project.craftTypes.includes("spinning")
                                    ) {
                                        temp.add(project);
                                    }
                                }
                            );
                        }
                        if (this.searchKnitting) {
                            Object.values(projectsData)[0].forEach(
                                (project) => {
                                    if (
                                        project.craftTypes.includes("knitting")
                                    ) {
                                        temp.add(project);
                                    }
                                }
                            );
                        }
                        if (this.searchSewing) {
                            Object.values(projectsData)[0].forEach(
                                (project) => {
                                    if (project.craftTypes.includes("sewing")) {
                                        temp.add(project);
                                    }
                                }
                            );
                        }
                        projectsData = Array.from(temp);

                        this.$store.commit("setUsersProjects", projectsData);
                        window.scrollTo(0, 0);
                    }
                }
            }
        );
    },
    data() {
        return {
            searchParam: "",
            searchStatus: null,
            searchSpinning: false,
            searchKnitting: false,
            searchSewing: false,
        };
    },
    methods: {
        redirectDetail(id) {
            this.$router.push(`/projects/${id}`);
        },
        reset() {
            this.searchParam = "";
            this.searchStatus = null;
            this.searchSpinning = false;
            this.searchKnitting = false;
            this.searchSewing = false;

            let projectsData = loadUsersProjects(this.$route.params.id).then(
                (projectsData) => {
                    if (projectsData) {
                        this.$store.commit("setUsersProjects", projectsData);
                    }
                }
            );
        },
        submit() {
            let projectsData = loadUsersProjects(this.$route.params.id).then(
                (projectsData) => {
                    if (projectsData) {
                        projectsData = projectsData.projects;
                    }
                    if (
                        !this.searchParam &&
                        !this.searchStatus &&
                        !this.searchSpinning &&
                        !this.searchKnitting &&
                        !this.searchSewing
                    ) {
                        window.scrollTo(0, 0);
                    } else {
                        if (this.searchParam) {
                            const temp = [];
                            projectsData.forEach((project) => {
                                if (
                                    project.title
                                        ?.toLowerCase()
                                        .includes(
                                            this.searchParam.toLowerCase()
                                        ) ||
                                    project.description
                                        ?.toLowerCase()
                                        .includes(
                                            this.searchParam.toLowerCase()
                                        )
                                ) {
                                    temp.push(project);
                                }
                            });
                            projectsData = temp;
                        }
                        if (this.searchStatus) {
                            const temp = [];
                            projectsData.forEach((project) => {
                                if (project.status == this.searchStatus) {
                                    temp.push(project);
                                }
                            });
                            projectsData = temp;
                        }

                        // Inclusive craft sort
                        if (this.searchSpinning || this.searchKnitting || this.searchSewing) {
                            const temp = new Set();
                            if (this.searchSpinning) {
                                projectsData.forEach((project) => {
                                    if (project.craftTypes.includes("spinning")) {
                                        temp.add(project);
                                    }
                                });
                            }
                            if (this.searchKnitting) {
                                projectsData.forEach((project) => {
                                    if (project.craftTypes.includes("knitting")) {
                                        temp.add(project);
                                    }
                                });
                            }
                            if (this.searchSewing) {
                                projectsData.forEach((project) => {
                                    if (project.craftTypes.includes("sewing")) {
                                        temp.add(project);
                                    }
                                });
                            }
                            projectsData = Array.from(temp);

                            this.$store.commit("setUsersProjects", projectsData);
                            window.scrollTo(0, 0);
                        } else {
                            this.$store.commit("setUsersProjects", projectsData);
                            window.scrollTo(0, 0);
                        }
                    }
                }
            );
        },
        createProject: function () {
            this.$router.push(`/projects/create`);
        },
    },
    mutations: {
        ...mapMutations,
    },
};

const loadUser = async (userId) => {
    const response = await fetch(`/api/users/${userId}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return false;
    }
};

const loadUsersProjects = async (userId) => {
    const response = await fetch(`/api/projects/users/${userId}`);
    if (response.ok) {
        const projectsData = await response.json();
        return projectsData;
    } else {
        return projectsData;
    }
};
</script>

<style scoped>
.projects-page {
    display: grid;
    grid-template-columns: 300px 1fr;
    column-gap: 4%;
}

.projects-page-left {
    min-height: calc(100vh - 70px);
    height: 100%;
    margin-bottom: 40px;
}

.projects-search-container {
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
    box-shadow: 2px 2px 2px var(--color-shadow);
    margin-top: 120px;
    margin-left: 28px;
    margin-bottom: 40px;
    position: sticky;
    top: 28px;
}

.projects-search-container > .header {
    width: 100%;
    background-color: var(--color-primary-contrast);
    margin: 0px;
    padding-top: 8px;
    padding-bottom: 8px;
    color: white;
    letter-spacing: 1px;
}

.projects-search-container > div {
    margin-top: 12px;
    margin-bottom: 12px;
    display: flex;
    flex-direction: column;
}

.projects-search-container > div > label {
    font-size: 15px;
}

.input-select {
    display: grid;
    grid-template-columns: 130px 135px;
}

.input-select-input {
    margin-left: 20px;
    margin-right: -10px;
}

input {
    font-size: 14px;
    font-family: "Open Sans", sans-serif;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
    padding-top: 6px;
    padding-bottom: 6px;
    padding-left: 10px;
    padding-right: 10px;
    margin-top: 8px;
    margin-bottom: 8px;
    margin-right: 20px;
    margin-left: 20px;
}

select {
    font-size: 14px;
    font-family: "Open Sans", sans-serif;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
    padding-top: 6px;
    padding-bottom: 6px;
    padding-left: 10px;
    padding-right: 10px;
    margin-top: 8px;
    margin-bottom: 8px;
    margin-right: 20px;
    margin-left: 20px;
}

button {
    border: 1px solid var(--color-shadow);
    background-color: white;
    border-radius: 4px;
    color: var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    margin-right: 20px;
    margin-left: 20px;
    margin-top: 4px;
    margin-bottom: 4px;
}

button:hover {
    cursor: pointer;
}

button:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.craft-options {
    display: grid;
    grid-template-columns: repeat(auto-fill, 110px);
    justify-content: space-between;
    row-gap: 2px;
    padding-top: 4px;
    margin-right: 20px;
    margin-left: 20px;
}

.craft-options > button {
    font-size: 12px;
    letter-spacing: 0px;
    margin: 2px;
}

.selected {
    background-color: var(--color-primary-contrast);
    color: white;
}

#submit-search {
    background-color: var(--color-primary-contrast);
    color: white;
    font-size: 16px;
}

#reset-search {
    border: 1px solid var(--color-shadow);
    background-color: white;
    border-radius: 4px;
    color: var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    margin-right: 20px;
    margin-left: 20px;
    margin-top: 4px;
    margin-bottom: 4px;
    font-size: 14px;
}

#reset-search:hover {
    cursor: pointer;
}

#reset-search:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.projects-body {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    text-align: left;
    padding-top: 40px;
    padding-bottom: 32px;
    padding-right: 8%;
    overflow: auto;
}

.projects-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.projects-header > h4 {
    display: flex;
    flex-direction: row;
    column-gap: 8px;
    align-items: center;
    background-color: var(--color-primary-contrast);
    color: white;
    padding-left: 12px;
    padding-right: 12px;
    padding-top: 6px;
    padding-bottom: 6px;
    border-radius: 16px;
    border: 1px solid var(--color-shadow);
    box-shadow: 2px 2px 2px var(--color-shadow);
    font-weight: normal;
}

.projects-header > h4:hover {
    cursor: pointer;
}

.projects-header > h4:active {
    box-shadow: 3px 3px 2px var(--color-shadow);
}

.projects-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, 160px);
    grid-gap: 12px;
    justify-content: space-between;
}

.projects-gallery-no-results {
    display: flex;
    flex-direction: column;
}

.project-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 160px;
    margin: 0px;
    margin: 8px;
}

.project-card > p {
    margin: 8px;
    font-size: 14px;
    text-align: center;
}

.card-image {
    width: 160px;
    height: 160px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.card-image:hover {
    cursor: pointer;
}

.card-header:hover {
    cursor: pointer;
    font-weight: bold;
}

#create-link {
    font-weight: bold;
}

#create-link:hover {
    cursor: pointer;
}
</style>
