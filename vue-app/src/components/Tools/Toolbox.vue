<template>
    <div class="toolbox">
        <div class="toolbox-left">
            <form class="toolbox-search-container" @submit.prevent="submit">
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
                        <option value="none" selected disabled hidden>
                            —
                        </option>
                        <option value="inStash">In stash</option>
                        <option value="inUse">In use</option>
                        <option value="loaned">Loaned</option>
                    </select>
                </div>
                <div>
                    <label>Filter by Craft</label>
                    <div class="craft-buttons">
                        <p
                            v-bind:class="{ active: searchSpinning }"
                            @click="toggleSpinning"
                        >
                            Spinning
                        </p>
                        <p
                            v-bind:class="{ active: searchWeaving }"
                            @click="toggleWeaving"
                        >
                            Weaving
                        </p>
                        <p
                            v-bind:class="{ active: searchKnitting }"
                            @click="toggleKnitting"
                        >
                            Knitting
                        </p>
                        <p
                            v-bind:class="{ active: searchCrocheting }"
                            @click="toggleCrocheting"
                        >
                            Crocheting
                        </p>
                        <p
                            v-bind:class="{ active: searchSewing }"
                            @click="toggleSewing"
                        >
                            Sewing
                        </p>
                        <p
                            v-bind:class="{ active: searchEmbroidery }"
                            @click="toggleEmbroidery"
                        >
                            Embroidery
                        </p>
                    </div>
                    <button id="submit-search">Search!</button>
                    <p id="reset-search" @click="reset">Reset Toolbox Search</p>
                </div>
            </form>
        </div>
        <div class="toolbox-body">
            <div class="toolbox-header">
                <h2>{{ $store.state.selectedUser?.username }}'s Toolbox</h2>
                <h4
                    @click="createTool"
                    v-if="$store.state.sessionUser?.id == $route.params.id"
                >
                    <i class="fas fa-plus-circle" /> Add new tool
                </h4>
            </div>
            <table v-if="$store.state.usersTools.length">
                <thead>
                    <tr>
                        <th />
                        <th>Image</th>
                        <th>Title</th>
                        <th>Acquired</th>
                        <th>Status</th>
                        <th>Spinning</th>
                        <th>Weaving</th>
                        <th>Knitting</th>
                        <th>Crocheting</th>
                        <th>Sewing</th>
                        <th>Embroidery</th>
                    </tr>
                </thead>
                <tbody v-if="$store.state.usersTools?.length > 0">
                    <tr v-for="tool in $store.state.usersTools" :key="tool.id">
                        <td
                            v-if="tool?.favorited"
                            @click.prevent="unfavorite"
                            :id="tool.id"
                        >
                            <i class="fas fa-star icon" :id="tool.id"></i>
                        </td>
                        <td v-else @click.prevent="favorite" :id="tool.id">
                            <i class="far fa-star icon" :id="tool.id"></i>
                        </td>
                        <td>
                            <img
                                v-if="tool.imageURL"
                                :src="tool.imageURL"
                                class="tool-image"
                                alt="User-uploaded tool image"
                            />
                        </td>
                        <td
                            v-if="
                                $store.state.sessionUser?.id == $route.params.id
                            "
                        >
                            <p
                                class="tool-title"
                                @click="redirectDetail(tool.id)"
                            >
                                {{ tool.title }}
                            </p>
                            <div class="edit-delete-div">
                                <p @click="editTool" v-bind:id="tool.id">
                                    EDIT
                                </p>
                                <p @click="deleteTool" v-bind:id="tool.id">
                                    DELETE
                                </p>
                            </div>
                        </td>
                        <td v-else>
                            <p
                                class="tool-title"
                                @click="redirectDetail(tool.id)"
                            >
                                {{ tool.title }}
                            </p>
                        </td>
                        <td v-if="tool?.acquired">
                            {{ tool.acquired.slice(5, 16) }}
                        </td>
                        <td v-else />
                        <td v-if="tool.status == 'inUse'">In Use</td>
                        <td v-else-if="tool.status == 'inStash'">In Stash</td>
                        <td v-else-if="tool.status == 'loaned'">Loaned</td>
                        <td v-else />
                        <td v-if="tool.forSpinning" class="centered">
                            <i class="fas fa-check-circle icon"></i>
                        </td>
                        <td v-else />
                        <td v-if="tool.forWeaving" class="centered">
                            <i class="fas fa-check-circle icon"></i>
                        </td>
                        <td v-else />
                        <td v-if="tool.forKnitting" class="centered">
                            <i class="fas fa-check-circle icon"></i>
                        </td>
                        <td v-else />
                        <td v-if="tool.forCrocheting" class="centered">
                            <i class="fas fa-check-circle icon"></i>
                        </td>
                        <td v-else />
                        <td v-if="tool.forSewing" class="centered">
                            <i class="fas fa-check-circle icon"></i>
                        </td>
                        <td v-else />
                        <td v-if="tool.forEmbroidery" class="centered">
                            <i class="fas fa-check-circle icon"></i>
                        </td>
                        <td v-else />
                    </tr>
                </tbody>
                <tbody v-else></tbody>
            </table>
            <div class="no-results" v-else>
                <h4>No results!</h4>
                <p>Maybe try broadening your search or <span id="create-link" @click="createTool">adding a new tool?</span></p>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "Toolbox",
    mounted() {
        this.$store.commit("clearSelectedUser");
        const data = loadUser(this.$route.params.id).then((data) => {
            if (data) {
                this.$store.commit("setSelectedUser", data);
            } else {
                this.$router.push("/404");
            }
        });
        const toolsData = loadUsersTools(this.$route.params.id).then(
            (toolsData) => {
                if (toolsData) {
                    this.$store.commit("setUsersTools", toolsData);
                    this.$store.commit("setUsersToolCategories", toolsData);
                }
            }
        );
    },
    data() {
        return {
            searchParam: "",
            searchStatus: "none",
            searchSpinning: false,
            searchWeaving: false,
            searchKnitting: false,
            searchCrocheting: false,
            searchSewing: false,
            searchEmbroidery: false,
        };
    },
    methods: {
        editTool: function (e) {
            this.$router.push(`/tools/${e.target.id}/edit`);
        },
        deleteTool: function (e) {
            this.$router.push(`/tools/${e.target.id}/delete`);
        },
        createTool: function () {
            this.$router.push(`/tools/create`);
        },
        toggleSpinning: function () {
            this.searchSpinning = !this.searchSpinning;
        },
        toggleWeaving: function () {
            this.searchWeaving = !this.searchWeaving;
        },
        toggleKnitting: function () {
            this.searchKnitting = !this.searchKnitting;
        },
        toggleCrocheting: function () {
            this.searchCrocheting = !this.searchCrocheting;
        },
        toggleSewing: function () {
            this.searchSewing = !this.searchSewing;
        },
        toggleEmbroidery: function () {
            this.searchEmbroidery = !this.searchEmbroidery;
        },
        submit() {
            let toolsData = loadUsersTools(this.$route.params.id).then(
                (toolsData) => {
                    if (toolsData) {
                        toolsData = toolsData.tools;
                    }
                    if (this.searchParam) {
                        const temp = [];
                        toolsData.forEach((tool) => {
                            if (
                                tool.title
                                    ?.toLowerCase()
                                    .includes(this.searchParam.toLowerCase()) ||
                                tool.description
                                    ?.toLowerCase()
                                    .includes(this.searchParam.toLowerCase())
                            ) {
                                temp.push(tool);
                            };
                        });
                        toolsData = temp;
                    };
                    if (this.searchStatus !== "none") {
                        const temp = [];
                        toolsData.forEach((tool) => {
                            if (tool.status == this.searchStatus) {
                                temp.push(tool);
                            }
                        });
                        toolsData = temp;
                    }
                    if (this.searchSpinning) {
                        const temp = [];
                        toolsData.forEach((tool) => {
                            if (tool.forSpinning) {
                                temp.push(tool);
                            }
                        });
                        toolsData = temp;
                    }
                    if (this.searchWeaving) {
                        const temp = [];
                        toolsData.forEach((tool) => {
                            if (tool.forWeaving) {
                                temp.push(tool);
                            }
                        });
                        toolsData = temp;
                    }
                    if (this.searchKnitting) {
                        const temp = [];
                        toolsData.forEach((tool) => {
                            if (tool.forKnitting) {
                                temp.push(tool);
                            }
                        });
                        toolsData = temp;
                    }
                    if (this.searchCrocheting) {
                        const temp = [];
                        toolsData.forEach((tool) => {
                            if (tool.forCrocheting) {
                                temp.push(tool);
                            }
                        });
                        toolsData = temp;
                    }
                    if (this.searchSewing) {
                        const temp = [];
                        toolsData.forEach((tool) => {
                            if (tool.forSewing) {
                                temp.push(tool);
                            }
                        });
                        toolsData = temp;
                    }
                    if (this.searchEmbroidery) {
                        const temp = [];
                        toolsData.forEach((tool) => {
                            if (tool.forEmbroidery) {
                                temp.push(tool);
                            }
                        });
                        toolsData = temp;
                    }
                    this.$store.commit("setUsersTools", toolsData);
                }
            );
        },
        reset() {
            const toolsData = loadUsersTools(this.$route.params.id).then(
                (toolsData) => {
                    if (toolsData) {
                        this.$store.commit("setUsersTools", toolsData);
                        this.$store.commit("setUsersToolCategories", toolsData);
                    }
                }
            );
        },
        async favorite(e) {
            const favoritedTool = {
                id: parseInt(e.target.id),
            };
            const response = await fetch("/api/tools/favorite", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(favoritedTool),
            }).then(async (response) => {
                const data = await response.json();
                const toolsData = loadUsersTools(data.userId).then(
                    (toolsData) => {
                        if (toolsData) {
                            this.$store.commit("setUsersTools", toolsData);
                            this.$store.commit(
                                "setUsersToolCategories",
                                toolsData
                            );
                        }
                    }
                );
            });
        },
        async unfavorite(e) {
            const unfavoritedTool = {
                id: parseInt(e.target.id),
            };
            const response = await fetch("/api/tools/unfavorite", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(unfavoritedTool),
            }).then(async (response) => {
                const data = await response.json();
                const toolsData = loadUsersTools(data.userId).then(
                    (toolsData) => {
                        if (toolsData) {
                            this.$store.commit("setUsersTools", toolsData);
                            this.$store.commit(
                                "setUsersToolCategories",
                                toolsData
                            );
                        }
                    }
                );
            });
        },
        redirectDetail(id) {
            this.$router.push(`/tools/${id}`);
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

const loadUsersTools = async (userId) => {
    const response = await fetch(`/api/tools/users/${userId}`);
    if (response.ok) {
        const toolsData = await response.json();
        return toolsData;
    } else {
        return false;
    }
};
</script>

<style scoped>
.toolbox {
    display: grid;
    grid-template-columns: 300px 1fr;
    column-gap: 4%;
}

.toolbox-left {
    min-height: calc(100vh - 70px);
    height: 100%;
    margin-bottom: 40px;
}

.toolbox-search-container {
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
    box-shadow: 2px 2px 2px var(--color-shadow);
    margin-top: 120px;
    margin-left: 32px;
    position: sticky;
    top: 32px;
}

.toolbox-search-container > .header {
    width: 100%;
    background-color: var(--color-primary-contrast);
    margin: 0px;
    padding-top: 8px;
    padding-bottom: 8px;
    color: white;
    letter-spacing: 1px;
}

.toolbox-search-container > div {
    margin-top: 12px;
    margin-bottom: 12px;
    display: flex;
    flex-direction: column;
}

.toolbox-search-container > div > label {
    font-size: 15px;
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

.craft-buttons {
    display: flex;
    flex-direction: column;
    margin-top: 6px;
    margin-bottom: 6px;
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

.craft-buttons > p {
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

.craft-buttons > p:hover {
    cursor: pointer;
}

.craft-buttons > p:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.craft-buttons > .active {
    background-color: var(--color-primary-contrast);
    color: white;
}

#submit-search {
    background-color: var(--color-primary-contrast);
    color: white;
    font-size: 16px;
}

.toolbox-body {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    text-align: left;
    padding-top: 40px;
    padding-bottom: 32px;
    padding-right: 8%;
    overflow: auto;
}

.toolbox-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.toolbox-header > h4 {
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

.toolbox-header > h4:hover {
    cursor: pointer;
}

.toolbox-header > h4:active {
    box-shadow: 3px 3px 2px var(--color-shadow);
}

table {
    overflow-x: scroll;
    border: 1px solid var(--color-shadow);
    border-collapse: collapse;
    font-family: "Open Sans", sans-serif;
}

th {
    border: 1px solid var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    padding-left: 8px;
    padding-right: 8px;
    background-color: var(--color-primary-contrast);
    color: white;
    letter-spacing: 1px;
    font-weight: normal;
}

td {
    font-size: 14px;
    border: 1px solid var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    padding-left: 8px;
    padding-right: 8px;
}

tbody > tr:hover {
    background-color: #f4eae6;
    font-weight: bold;
}

.edit-delete-div {
    margin-top: -10px;
    margin-bottom: 8px;
    font-size: 11px;
    display: flex;
    flex-direction: row;
    column-gap: 8px;
}

.tool-image {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.tool-title:hover {
    cursor: pointer;
}

.edit-delete-div > p {
    margin: 0px;
}

.edit-delete-div > p:hover {
    color: var(--color-primary-contrast);
    cursor: pointer;
    font-weight: bold;
}

.icon {
    justify-self: center;
    font-size: 16px;
}

.icon:hover {
    cursor: pointer;
}

.centered {
    text-align: center;
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

.no-results {
    display: flex;
    flex-direction: column;
}

#create-link {
    font-weight: bold;
}

#create-link:hover {
    cursor: pointer;
}
</style>
