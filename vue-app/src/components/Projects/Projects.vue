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
                    <div id="craft-options">
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
                            v-bind:class="{ selected: searchWeaving }"
                            @click.prevent="
                                this.searchWeaving = !this.searchWeaving
                            "
                        >
                            Weaving
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
                            v-bind:class="{ selected: searchCrocheting }"
                            @click.prevent="
                                this.searchCrocheting = !this.searchCrocheting
                            "
                        >
                            Crocheting
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
                        <button
                            type="button"
                            v-bind:class="{ selected: searchEmbroidery }"
                            @click.prevent="
                                this.searchEmbroidery = !this.searchEmbroidery
                            "
                        >
                            Embroidery
                        </button>
                    </div>
                </div>
                <div v-if="this.searchKnitting">
                    <label id="needle-options-label"
                        >Filter by Needle Size:</label
                    >
                    <div id="needle-options">
                        <button
                            v-bind:class="{ selected: searchKnitting01 }"
                            @click.prevent="
                                this.searchKnitting01 = !this.searchKnitting01
                            "
                        >
                            000 (1.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting02 }"
                            @click.prevent="
                                this.searchKnitting02 = !this.searchKnitting02
                            "
                        >
                            00 (1.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting03 }"
                            @click.prevent="
                                this.searchKnitting03 = !this.searchKnitting03
                            "
                        >
                            0 (2 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting04 }"
                            @click.prevent="
                                this.searchKnitting04 = !this.searchKnitting04
                            "
                        >
                            1 (2.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting05 }"
                            @click.prevent="
                                this.searchKnitting05 = !this.searchKnitting05
                            "
                        >
                            2 (2.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting06 }"
                            @click.prevent="
                                this.searchKnitting06 = !this.searchKnitting06
                            "
                        >
                            3 mm
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting07 }"
                            @click.prevent="
                                this.searchKnitting07 = !this.searchKnitting07
                            "
                        >
                            3 (3.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting08 }"
                            @click.prevent="
                                this.searchKnitting08 = !this.searchKnitting08
                            "
                        >
                            4 (3.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting09 }"
                            @click.prevent="
                                this.searchKnitting09 = !this.searchKnitting09
                            "
                        >
                            5 (3.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting10 }"
                            @click.prevent="
                                this.searchKnitting10 = !this.searchKnitting10
                            "
                        >
                            6 (4 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting11 }"
                            @click.prevent="
                                this.searchKnitting11 = !this.searchKnitting11
                            "
                        >
                            7 (4.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting12 }"
                            @click.prevent="
                                this.searchKnitting12 = !this.searchKnitting12
                            "
                        >
                            8 (5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting13 }"
                            @click.prevent="
                                this.searchKnitting13 = !this.searchKnitting13
                            "
                        >
                            9 (5.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting14 }"
                            @click.prevent="
                                this.searchKnitting14 = !this.searchKnitting14
                            "
                        >
                            10 (6 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting15 }"
                            @click.prevent="
                                this.searchKnitting15 = !this.searchKnitting15
                            "
                        >
                            10 1/2 (6.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting16 }"
                            @click.prevent="
                                this.searchKnitting16 = !this.searchKnitting16
                            "
                        >
                            7 mm
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting17 }"
                            @click.prevent="
                                this.searchKnitting17 = !this.searchKnitting17
                            "
                        >
                            11 (8 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting18 }"
                            @click.prevent="
                                this.searchKnitting18 = !this.searchKnitting18
                            "
                        >
                            13 (9 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting19 }"
                            @click.prevent="
                                this.searchKnitting19 = !this.searchKnitting19
                            "
                        >
                            15 (10 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting20 }"
                            @click.prevent="
                                this.searchKnitting20 = !this.searchKnitting20
                            "
                        >
                            17 (12.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting21 }"
                            @click.prevent="
                                this.searchKnitting21 = !this.searchKnitting21
                            "
                        >
                            19 (15 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting22 }"
                            @click.prevent="
                                this.searchKnitting22 = !this.searchKnitting22
                            "
                        >
                            35 (19 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting23 }"
                            @click.prevent="
                                this.searchKnitting23 = !this.searchKnitting23
                            "
                        >
                            50 (25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchKnitting24 }"
                            @click.prevent="
                                this.searchKnitting24 = !this.searchKnitting24
                            "
                        >
                            70 (35 mm)
                        </button>
                    </div>
                </div>
                <div>
                    <label id="needle-options-label"
                        >Filter by Hook Size:</label
                    >
                    <div id="needle-options">
                        <button
                            v-bind:class="{ selected: searchCrochet01 }"
                            @click.prevent="
                                this.searchCrochet01 = !this.searchCrochet01
                            "
                        >
                            B-1 (2.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet02 }"
                            @click.prevent="
                                this.searchCrochet02 = !this.searchCrochet02
                            "
                        >
                            2.5mm
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet03 }"
                            @click.prevent="
                                this.searchCrochet03 = !this.searchCrochet03
                            "
                        >
                            C-2 (2.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet04 }"
                            @click.prevent="
                                this.searchCrochet04 = !this.searchCrochet04
                            "
                        >
                            D (3.125 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet05 }"
                            @click.prevent="
                                this.searchCrochet05 = !this.searchCrochet05
                            "
                        >
                            D-3 (3.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet06 }"
                            @click.prevent="
                                this.searchCrochet06 = !this.searchCrochet06
                            "
                        >
                            E-4 (3.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet07 }"
                            @click.prevent="
                                this.searchCrochet07 = !this.searchCrochet07
                            "
                        >
                            F-5 (3.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet08 }"
                            @click.prevent="
                                this.searchCrochet08 = !this.searchCrochet08
                            "
                        >
                            G-6 (4 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet09 }"
                            @click.prevent="
                                this.searchCrochet09 = !this.searchCrochet09
                            "
                        >
                            G (4.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet10 }"
                            @click.prevent="
                                this.searchCrochet10 = !this.searchCrochet10
                            "
                        >
                            7 (4.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet11 }"
                            @click.prevent="
                                this.searchCrochet11 = !this.searchCrochet11
                            "
                        >
                            H-8 (5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet12 }"
                            @click.prevent="
                                this.searchCrochet12 = !this.searchCrochet12
                            "
                        >
                            I (5.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet13 }"
                            @click.prevent="
                                this.searchCrochet13 = !this.searchCrochet13
                            "
                        >
                            J (5.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet14 }"
                            @click.prevent="
                                this.searchCrochet14 = !this.searchCrochet14
                            "
                        >
                            J-10 (6 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet15 }"
                            @click.prevent="
                                this.searchCrochet15 = !this.searchCrochet15
                            "
                        >
                            K-10 1/2 (6.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet16 }"
                            @click.prevent="
                                this.searchCrochet16 = !this.searchCrochet16
                            "
                        >
                            L-11 (8 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet17 }"
                            @click.prevent="
                                this.searchCrochet17 = !this.searchCrochet17
                            "
                        >
                            M/N-13 (9 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet18 }"
                            @click.prevent="
                                this.searchCrochet18 = !this.searchCrochet18
                            "
                        >
                            N/P-15 (10 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet19 }"
                            @click.prevent="
                                this.searchCrochet19 = !this.searchCrochet19
                            "
                        >
                            P-16 (11.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet20 }"
                            @click.prevent="
                                this.searchCrochet20 = !this.searchCrochet20
                            "
                        >
                            P/Q (15 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet21 }"
                            @click.prevent="
                                this.searchCrochet21 = !this.searchCrochet21
                            "
                        >
                            Q (16 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet22 }"
                            @click.prevent="
                                this.searchCrochet22 = !this.searchCrochet22
                            "
                        >
                            S (19 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet23 }"
                            @click.prevent="
                                this.searchCrochet23 = !this.searchCrochet23
                            "
                        >
                            T/U/X (25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: searchCrochet24 }"
                            @click.prevent="
                                this.searchCrochet24 = !this.searchCrochet24
                            "
                        >
                            T/X (30 mm)
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
                <h2>{{ user?.username }}'s Projects</h2>
                <h4
                    @click="createProject"
                    v-if="$store.state.sessionUser?.id == $route.params.id"
                >
                    <i class="fas fa-plus-circle" />Add New Project
                </h4>
            </div>
            <div class="projects-gallery" v-if="usersProjects?.length">
                <div
                    class="project-card"
                    v-for="project in usersProjects"
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
export default {
    name: "Projects",
    mounted() {
        const data = loadUser(this.$route.params.id).then((data) => {
            if (data) {
                this.user = data;
            } else {
                this.$router.push("/login");
            }
        });
        const projectsData = loadUsersProjects(this.$route.params.id).then(
            (projectsData) => {
                if (projectsData) {
                    if (Array.isArray(projectsData)) {
                        this.usersProjects = projectsData;
                    } else {
                        this.usersProjects = Object.values(projectsData)[0];
                    }
                    if (this.$route.params.craftParam) {
                        if (this.$route.params.craftParam == "spinning") {
                            this.searchSpinning = true;
                        } else if (this.$route.params.craftParam == "weaving") {
                            this.searchWeaving = true;
                        } else if (
                            this.$route.params.craftParam == "knitting"
                        ) {
                            this.searchKnitting = true;
                        } else if (
                            this.$route.params.craftParam == "crocheting"
                        ) {
                            this.searchCrocheting = true;
                        } else if (this.$route.params.craftParam == "sewing") {
                            this.searchSewing = true;
                        } else if (
                            this.$route.params.craftParam == "embroidery"
                        ) {
                            this.searchEmbroidery = true;
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
                        if (this.searchWeaving) {
                            Object.values(projectsData)[0].forEach(
                                (project) => {
                                    if (
                                        project.craftTypes.includes("weaving")
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
                        if (this.searchCrocheting) {
                            Object.values(projectsData)[0].forEach(
                                (project) => {
                                    if (
                                        project.craftTypes.includes(
                                            "crocheting"
                                        )
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
                        if (this.searchEmbroidery) {
                            Object.values(projectsData)[0].forEach(
                                (project) => {
                                    if (
                                        project.craftTypes.includes(
                                            "embroidery"
                                        )
                                    ) {
                                        temp.add(project);
                                    }
                                }
                            );
                        }
                        projectsData = Array.from(temp);

                        this.usersProjects = projectsData;
                        window.scrollTo(0, 0);
                    }
                }
            }
        );
    },
    data() {
        return {
            user: null,
            searchParam: "",
            searchStatus: null,
            searchSpinning: false,
            searchWeaving: false,

            searchKnitting: false,
            searchKnitting01: false,
            searchKnitting02: false,
            searchKnitting03: false,
            searchKnitting04: false,
            searchKnitting05: false,
            searchKnitting06: false,
            searchKnitting07: false,
            searchKnitting08: false,
            searchKnitting09: false,
            searchKnitting10: false,
            searchKnitting11: false,
            searchKnitting12: false,
            searchKnitting13: false,
            searchKnitting14: false,
            searchKnitting15: false,
            searchKnitting16: false,
            searchKnitting17: false,
            searchKnitting18: false,
            searchKnitting19: false,
            searchKnitting20: false,
            searchKnitting21: false,
            searchKnitting22: false,
            searchKnitting23: false,
            searchKnitting24: false,

            searchCrocheting: false,
            searchCrochet01: false,
            searchCrochet02: false,
            searchCrochet03: false,
            searchCrochet04: false,
            searchCrochet05: false,
            searchCrochet06: false,
            searchCrochet07: false,
            searchCrochet08: false,
            searchCrochet09: false,
            searchCrochet10: false,
            searchCrochet11: false,
            searchCrochet12: false,
            searchCrochet13: false,
            searchCrochet14: false,
            searchCrochet15: false,
            searchCrochet16: false,
            searchCrochet17: false,
            searchCrochet18: false,
            searchCrochet19: false,
            searchCrochet20: false,
            searchCrochet21: false,
            searchCrochet22: false,
            searchCrochet23: false,
            searchCrochet24: false,

            searchSewing: false,
            searchEmbroidery: false,
            usersProjects: [],
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
            this.searchWeaving = false;

            this.searchKnitting = false;
            this.searchKnitting01 = false;
            this.searchKnitting02 = false;
            this.searchKnitting03 = false;
            this.searchKnitting04 = false;
            this.searchKnitting05 = false;
            this.searchKnitting06 = false;
            this.searchKnitting07 = false;
            this.searchKnitting08 = false;
            this.searchKnitting09 = false;
            this.searchKnitting10 = false;
            this.searchKnitting10 = false;
            this.searchKnitting11 = false;
            this.searchKnitting12 = false;
            this.searchKnitting13 = false;
            this.searchKnitting14 = false;
            this.searchKnitting15 = false;
            this.searchKnitting16 = false;
            this.searchKnitting17 = false;
            this.searchKnitting18 = false;
            this.searchKnitting19 = false;
            this.searchKnitting20 = false;
            this.searchKnitting21 = false;
            this.searchKnitting22 = false;
            this.searchKnitting23 = false;
            this.searchKnitting24 = false;

            this.searchCrocheting = false;
            this.searchCrochet01 = false;
            this.searchCrochet02 = false;
            this.searchCrochet03 = false;
            this.searchCrochet04 = false;
            this.searchCrochet05 = false;
            this.searchCrochet06 = false;
            this.searchCrochet07 = false;
            this.searchCrochet08 = false;
            this.searchCrochet09 = false;
            this.searchCrochet10 = false;
            this.searchCrochet11 = false;
            this.searchCrochet12 = false;
            this.searchCrochet13 = false;
            this.searchCrochet14 = false;
            this.searchCrochet15 = false;
            this.searchCrochet16 = false;
            this.searchCrochet17 = false;
            this.searchCrochet18 = false;
            this.searchCrochet19 = false;
            this.searchCrochet20 = false;
            this.searchCrochet21 = false;
            this.searchCrochet22 = false;
            this.searchCrochet23 = false;
            this.searchCrochet24 = false;

            this.searchSewing = false;
            this.searchEmbroidery = false;

            let projectsData = loadUsersProjects(this.$route.params.id).then(
                (projectsData) => {
                    if (projectsData) {
                        if (Array.isArray(projectsData)) {
                            this.usersProjects = projectsData;
                        } else {
                            this.usersProjects = Object.values(projectsData)[0];
                        }
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
                        !this.searchWeaving &&
                        !this.searchKnitting &&
                        !this.searchCrocheting &&
                        !this.searchSewing &&
                        !this.searchEmbroidery
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
                        if (
                            this.searchSpinning ||
                            this.searchWeaving ||
                            this.searchKnitting ||
                            this.searchCrocheting ||
                            this.searchSewing ||
                            this.searchEmbroidery
                        ) {
                            const temp = new Set();
                            if (this.searchSpinning) {
                                projectsData.forEach((project) => {
                                    if (
                                        project.craftTypes.includes("spinning")
                                    ) {
                                        temp.add(project);
                                    }
                                });
                            }
                            if (this.searchWeaving) {
                                projectsData.forEach((project) => {
                                    if (
                                        project.craftTypes.includes("weaving")
                                    ) {
                                        temp.add(project);
                                    }
                                });
                            }
                            if (this.searchKnitting) {
                                projectsData.forEach((project) => {
                                    if (
                                        project.craftTypes.includes("knitting")
                                    ) {
                                        temp.add(project);
                                    }
                                });
                            }
                            if (this.searchCrocheting) {
                                projectsData.forEach((project) => {
                                    if (
                                        project.craftTypes.includes(
                                            "crocheting"
                                        )
                                    ) {
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
                            if (this.searchEmbroidery) {
                                projectsData.forEach((project) => {
                                    if (
                                        project.craftTypes.includes(
                                            "embroidery"
                                        )
                                    ) {
                                        temp.add(project);
                                    }
                                });
                            }
                            projectsData = Array.from(temp);
                        }

                        // Knitting needle size sort
                        if (
                            this.searchKnitting01 ||
                            this.searchKnitting02 ||
                            this.searchKnitting03 ||
                            this.searchKnitting04 ||
                            this.searchKnitting05 ||
                            this.searchKnitting06 ||
                            this.searchKnitting07 ||
                            this.searchKnitting08 ||
                            this.searchKnitting09 ||
                            this.searchKnitting10 ||
                            this.searchKnitting11 ||
                            this.searchKnitting12 ||
                            this.searchKnitting13 ||
                            this.searchKnitting14 ||
                            this.searchKnitting15 ||
                            this.searchKnitting16 ||
                            this.searchKnitting17 ||
                            this.searchKnitting18 ||
                            this.searchKnitting19 ||
                            this.searchKnitting20 ||
                            this.searchKnitting21 ||
                            this.searchKnitting22 ||
                            this.searchKnitting23 ||
                            this.searchKnitting24
                        ) {
                            const temp = new Set();
                            projectsData.forEach((project) => {
                                const needlesArr =
                                    project.needleSizes?.split(",");
                                if (
                                    this.searchKnitting01 &&
                                    needlesArr.includes("1.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting02 &&
                                    needlesArr.includes("1.75")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting03 &&
                                    needlesArr.includes("2")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting04 &&
                                    needlesArr.includes("2.25")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting05 &&
                                    needlesArr.includes("2.75")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting06 &&
                                    needlesArr.includes("3")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting07 &&
                                    needlesArr.includes("3.25")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting08 &&
                                    needlesArr.includes("3.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting09 &&
                                    needlesArr.includes("3.75")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting10 &&
                                    needlesArr.includes("4")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting11 &&
                                    needlesArr.includes("4.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting12 &&
                                    needlesArr.includes("5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting13 &&
                                    needlesArr.includes("5.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting14 &&
                                    needlesArr.includes("6")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting15 &&
                                    needlesArr.includes("6.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting16 &&
                                    needlesArr.includes("7")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting17 &&
                                    needlesArr.includes("8")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting18 &&
                                    needlesArr.includes("9")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting19 &&
                                    needlesArr.includes("10")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting20 &&
                                    needlesArr.includes("12.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting21 &&
                                    needlesArr.includes("15")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting22 &&
                                    needlesArr.includes("19")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting23 &&
                                    needlesArr.includes("25")
                                )
                                    temp.add(project);
                                if (
                                    this.searchKnitting24 &&
                                    needlesArr.includes("35")
                                )
                                    temp.add(project);
                            });
                            projectsData = Array.from(temp);
                        }

                        // Crochet hook size sort
                        if (
                            this.searchCrochet01 ||
                            this.searchCrochet02 ||
                            this.searchCrochet03 ||
                            this.searchCrochet04 ||
                            this.searchCrochet05 ||
                            this.searchCrochet06 ||
                            this.searchCrochet07 ||
                            this.searchCrochet08 ||
                            this.searchCrochet09 ||
                            this.searchCrochet10 ||
                            this.searchCrochet11 ||
                            this.searchCrochet12 ||
                            this.searchCrochet13 ||
                            this.searchCrochet14 ||
                            this.searchCrochet15 ||
                            this.searchCrochet16 ||
                            this.searchCrochet17 ||
                            this.searchCrochet18 ||
                            this.searchCrochet19 ||
                            this.searchCrochet20 ||
                            this.searchCrochet21 ||
                            this.searchCrochet22 ||
                            this.searchCrochet23 ||
                            this.searchCrochet24
                        ) {
                            const temp = new Set();
                            projectsData.forEach((project) => {
                                const hooksArr = project.hookSizes?.split(",");
                                if (
                                    this.searchCrochet01 &&
                                    hooksArr.includes("2.25")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet02 &&
                                    hooksArr.includes("2.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet03 &&
                                    hooksArr.includes("2.75")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet04 &&
                                    hooksArr.includes("3.125")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet05 &&
                                    hooksArr.includes("3.25")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet06 &&
                                    hooksArr.includes("3.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet07 &&
                                    hooksArr.includes("3.75")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet08 &&
                                    hooksArr.includes("4")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet09 &&
                                    hooksArr.includes("4.25")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet10 &&
                                    hooksArr.includes("4.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet11 &&
                                    hooksArr.includes("5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet12 &&
                                    hooksArr.includes("5.25")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet13 &&
                                    hooksArr.includes("5.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet14 &&
                                    hooksArr.includes("6")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet15 &&
                                    hooksArr.includes("6.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet16 &&
                                    hooksArr.includes("8")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet17 &&
                                    hooksArr.includes("9")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet18 &&
                                    hooksArr.includes("10")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet19 &&
                                    hooksArr.includes("11.5")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet20 &&
                                    hooksArr.includes("15")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet21 &&
                                    hooksArr.includes("16")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet22 &&
                                    hooksArr.includes("19")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet23 &&
                                    hooksArr.includes("25")
                                )
                                    temp.add(project);
                                if (
                                    this.searchCrochet24 &&
                                    hooksArr.includes("30")
                                )
                                    temp.add(project);
                            });
                            projectsData = Array.from(temp);
                        }

                        this.usersProjects = projectsData;
                        window.scrollTo(0, 0);
                    }
                }
            );
        },
        createProject: function () {
            this.$router.push(`/projects/create`);
        },
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
    grid-template-columns: 380px 1fr;
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
    margin-top: 68px;
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

#craft-options {
    display: grid;
    grid-template-columns: repeat(auto-fill, 100px);
    justify-content: space-between;
    row-gap: 2px;
    padding-top: 4px;
    margin-right: 20px;
    margin-left: 20px;
}

#craft-options > button {
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

#needle-options-label {
    margin-top: 8px;
}

#needle-options {
    display: grid;
    grid-template-columns: 105px 105px 105px;
    column-gap: 6px;
    row-gap: 6px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 8px;
}

#needle-options > button {
    font-size: 11px;
    letter-spacing: 0px;
    margin: 0px;
}
</style>
