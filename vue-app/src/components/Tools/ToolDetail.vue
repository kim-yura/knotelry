<template>
    <div class="tool-detail">
        <div class="left">
            <img
                v-if="this.imageURL"
                class="detail-image"
                :src="this.imageURL"
                alt="User-uploaded image of tool"
            />
            <img
                v-else
                class="detail-image"
                src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                alt="No image found"
            />
            <div class="tool-header">
                <i
                    class="fas fa-star icon"
                    v-if="
                        this.favorited &&
                        $store.state.sessionUser?.id == this.user?.id
                    "
                    @click.prevent="unfavorite"
                />
                <i
                    class="far fa-star icon"
                    v-else-if="$store.state.sessionUser?.id == this.user?.id"
                    @click.prevent="favorite"
                />
                <h2>{{ this.title }}</h2>
            </div>
            <div
                v-if="$store.state.sessionUser?.id == this.user?.id"
                class="tool-options"
            >
                <button @click="editTool">Edit Tool</button>
                <button @click="deleteTool">Delete Tool</button>
            </div>
        </div>
        <div class="right">
            <div class="detail-text">
                <div class="text-label">Description:</div>
                <div class="text-content" v-if="this.description">
                    {{ this.description }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Date Acquired:</div>
                <div class="text-content" v-if="this.acquired">
                    {{ this.acquired.slice(5, 16) }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Tagged Crafts:</div>
                <div class="text-content" v-if="this.taggedCrafts?.length">
                    {{ this.taggedCrafts.join(", ") }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Status:</div>
                <div class="text-content" v-if="this.status == 'inUse'">
                    In Use
                </div>
                <div class="text-content" v-else-if="this.status == 'inStash'">
                    In Stash
                </div>
                <div class="text-content" v-else-if="this.status == 'loaned'">
                    Loaned
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="divider" />
            <div class="detail-text">
                <div class="text-label">Linked Projects:</div>
                <div
                    class="linked-project-gallery"
                    v-if="this.linkedProjects?.length"
                >
                    <div
                        class="project"
                        v-for="project in linkedProjects"
                        :key="project.id"
                    >
                        <img
                            class="project-image"
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            alt="User-uploaded image of project"
                            @click.prevent="redirectProject(project.id)"
                        />
                        <img
                            class="project-image"
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                            @click.prevent="redirectProject(project.id)"
                        />
                        <p
                            class="project-link"
                            @click.prevent="redirectProject(project.id)"
                        >
                            {{ project.title }}
                        </p>
                    </div>
                </div>
                <div class="text-content" v-else>No linked projects</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ToolDetail",
    mounted() {
        const data = loadTool(this.$route.params.toolId).then((data) => {
            if (data) {
                this.acquired = data.acquired;
                this.description = data.description;
                this.favorited = data.favorited;
                this.forCrocheting = data.forCrocheting;
                this.forEmbroidery = data.forEmbroidery;
                this.forKnitting = data.forKnitting;
                this.forSewing = data.forSewing;
                this.forSpinning = data.forSpinning;
                this.forWeaving = data.forWeaving;
                this.imageURL = data.imageURL;
                this.status = data.status;
                this.title = data.title;
                this.user = data.user;

                if (this.forCrocheting) this.taggedCrafts.push("Crocheting");
                if (this.forEmbroidery) this.taggedCrafts.push("Embroidery");
                if (this.forKnitting) this.taggedCrafts.push("Knitting");
                if (this.forSewing) this.taggedCrafts.push("Sewing");
                if (this.forSpinning) this.taggedCrafts.push("Spinning");
                if (this.forWeaving) this.taggedCrafts.push("Weaving");
            } else {
                this.$router.push("/404");
            }
            const projectsData = loadLinkedProjects(
                parseInt(this.$route.params.toolId)
            ).then((projectsData) => {
                if (projectsData) {
                    this.linkedProjects = Object.values(projectsData)[0];
                }
            });
        });
    },
    data() {
        return {
            acquired: null,
            description: null,
            favorited: false,
            forCrocheting: false,
            forEmbroidery: false,
            forKnitting: false,
            forSewing: false,
            forSpinning: false,
            forWeaving: false,
            imageURL: null,
            status: null,
            title: null,
            user: null,
            taggedCrafts: [],

            linkedProjects: null,
        };
    },
    methods: {
        async favorite() {
            const favoritedTool = {
                id: this.$route.params.toolId,
            };
            const response = await fetch("/api/tools/favorite", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(favoritedTool),
            }).then(async (response) => {
                const data = await response.json();
                const toolDetail = loadTool(data.id).then((data) => {
                    if (data) {
                        this.favorited = data.favorited;
                    } else {
                        this.$router.push("/404");
                    }
                });
            });
        },
        async unfavorite() {
            const unfavoritedTool = {
                id: this.$route.params.toolId,
            };
            const response = await fetch("/api/tools/unfavorite", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(unfavoritedTool),
            }).then(async (response) => {
                const data = await response.json();
                const toolDetail = loadTool(data.id).then((data) => {
                    if (data) {
                        this.favorited = data.favorited;
                    } else {
                        this.$router.push("/404");
                    }
                });
            });
        },
        editTool: function () {
            this.$router.push(`/tools/${this.$route.params.toolId}/edit`);
        },
        deleteTool: function () {
            this.$router.push(`/tools/${this.$route.params.toolId}/delete`);
        },
        redirectProject(id) {
            this.$router.push(`/projects/${id}`);
        },
    },
};

const loadTool = async (toolId) => {
    const response = await fetch(`/api/tools/${toolId}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return false;
    }
};

const loadLinkedProjects = async (toolId) => {
    const response = await fetch(`/api/tools/${toolId}/projects`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return data;
    }
};
</script>

<style scoped>
.tool-detail {
    display: grid;
    grid-template-columns: 400px 1fr;
    padding-left: 14%;
    padding-right: 14%;
    padding-top: 60px;
}

.left {
    display: flex;
    flex-direction: column;
    padding-bottom: 32px;
    padding-right: 8%;
    padding-left: 8%;
}

.detail-image {
    margin-left: auto;
    margin-right: auto;
    height: 300px;
    width: 300px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 6px;
}

.tool-header {
    margin-left: auto;
    margin-right: auto;
    width: 300px;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: left;
    justify-content: space-between;
    column-gap: 20px;
}

.icon {
    text-align: right;
}

.icon:hover {
    cursor: pointer;
}

.tool-options {
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-direction: row;
    column-gap: 4px;
}

button {
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    width: 146px;
    padding-top: 4px;
    padding-bottom: 4px;
    border-radius: 4px;
    border: 1px solid var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
    background-color: var(--color-primary-contrast);
    color: white;
    font-size: 16px;
    letter-spacing: 2px;
}

button:hover {
    cursor: pointer;
}

button:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.right {
    display: flex;
    flex-direction: column;
}

.detail-text {
    display: grid;
    grid-template-columns: 160px 1fr;
    text-align: justify;
    font-size: 14px;
    margin-bottom: 12px;
}

.text-content {
    text-align: left;
}

.linked-project-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, 100px);
    grid-gap: 12px;
    justify-content: space-between;
}

.project {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.project-image {
    width: 100px;
    height: 100px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.project-image:hover {
    cursor: pointer;
}

.project-link {
    margin-top: 0px;
    text-align: center;
}

.project-link:hover {
    font-weight: bold;
    cursor: pointer;
}

.divider {
    border-top: 1px solid var(--color-shadow);
    margin-top: 10px;
    margin-bottom: 16px;
    padding: 0px;
}

</style>
