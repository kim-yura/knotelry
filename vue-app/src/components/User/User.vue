<template>
    <div v-if="user?.id" class="user-body">
        <div class="user-left">
            <h3>{{ user?.username }}</h3>
            <div class="pronouns-container">
                <p class="pronouns" v-if="user?.pronouns_she">she/her/hers</p>
                <p class="pronouns" v-if="user?.pronouns_he">he/him/his</p>
                <p class="pronouns" v-if="user?.pronouns_they">
                    they/them/theirs
                </p>
                <span class="pronouns" v-if="user?.pronouns_custom?.length">
                    <p
                        v-for="pronoun in user?.pronouns_custom.split(',')"
                        :key="pronoun"
                        class="pronouns"
                    >
                        {{ pronoun }}
                    </p>
                </span>
            </div>
            <button
                v-if="$store.state.sessionUser?.id == user?.id"
                @click="edit"
            >
                Edit Profile
            </button>
            <img
                v-if="user?.profile_pic_url"
                :src="user?.profile_pic_url"
                class="user-profile"
                alt="User profile"
            />
            <!-- SOCIAL LINKS -->
            <div class="social-container" v-if="user?.instagram">
                <img
                    src="https://upload.wikimedia.org/wikipedia/commons/5/58/Instagram-Icon.png"
                    class="icon"
                    alt="Instagram icon"
                />
                <div class="social-text">
                    <p>Instagram:</p>
                    <a
                        v-bind:href="
                            'https://www.instagram.com/' + user?.instagram
                        "
                        target="_blank"
                        >{{ user?.instagram }}
                    </a>
                </div>
            </div>
            <div class="social-container" v-if="user?.twitter">
                <img
                    src="https://upload.wikimedia.org/wikipedia/commons/4/4f/Twitter-logo.svg"
                    class="icon"
                    alt="Twitter icon"
                />
                <div class="social-text">
                    <p>Twitter:</p>
                    <a
                        v-bind:href="'https://twitter.com/' + user?.twitter"
                        target="_blank"
                        >{{ user?.twitter }}
                    </a>
                </div>
            </div>
            <div class="social-container" v-if="user?.kofi">
                <img
                    src="https://uploads-ssl.webflow.com/5c14e387dab576fe667689cf/61e1116779fc0a9bd5bdbcc7_Frame%206.png"
                    class="icon"
                    alt="Ko-fi icon"
                />
                <div class="social-text">
                    <p>Ko-fi:</p>
                    <a
                        v-bind:href="'https://ko-fi.com/' + user?.kofi"
                        target="_blank"
                        >{{ user?.kofi }}
                    </a>
                </div>
            </div>
            <div class="social-container" v-if="user?.website">
                <img
                    src="https://w7.pngwing.com/pngs/549/715/png-transparent-web-development-logo-website-web-design-symmetry-internet-thumbnail.png"
                    class="icon"
                    alt="Web icon"
                />
                <div class="social-text">
                    <p>Website:</p>
                    <a v-bind:href="'https://' + user?.website" target="_blank"
                        >{{ user?.website }}
                    </a>
                </div>
            </div>

            <!-- Toggle query for crafts -->
            <div class="crafts-container">
                <p class="header">{{ user?.username }}'s Crafts</p>
                <!-- Each button can maybe redirect to that user's craft notebook -->
                <button v-if="user?.is_spinner" class="craft-button">
                    spinning
                </button>
                <button v-if="user?.is_weaver" class="craft-button">
                    weaving
                </button>
                <button v-if="user?.is_knitter" class="craft-button">
                    knitting
                </button>
                <button v-if="user?.is_crocheter" class="craft-button">
                    crocheting
                </button>
                <button v-if="user?.is_sewist" class="craft-button">
                    sewing
                </button>
                <button v-if="user?.is_embroiderer" class="craft-button">
                    embroidery
                </button>
            </div>
        </div>
        <div class="user-main">
            <div class="user-text">
                <div class="user-text-label">Bio:</div>
                <div class="user-text-content" v-if="user?.bio?.length">
                    {{ user?.bio }}
                </div>
                <div class="user-text-content" v-else>—</div>
                <div class="user-text-label">Crafting Journey:</div>
                <div
                    class="user-text-content"
                    v-if="user?.crafting_journey?.length"
                >
                    {{ user?.crafting_journey }}
                </div>
                <div class="text-content" v-else>—</div>
                <div class="user-text-label">Roles:</div>
                <div class="user-text-content" v-if="user?.roles?.length">
                    {{ user?.roles }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="divider" />
            <div class="user-gallery-container">
                <div class="user-gallery-header">
                    <h4>{{ user?.username }}'s Gallery</h4>
                </div>
                <div class="user-gallery" v-if="usersPhotos?.length > 0">
                    <div
                        v-for="image in usersPhotos"
                        :key="image.id"
                        class="gallery-image-container"
                    >
                        <img
                            :key="image.id"
                            :src="image.imageURL"
                            alt="Gallery image"
                        />
                        <i
                            class="fas fa-trash-alt"
                            v-if="$store.state.sessionUser?.id == user?.id"
                            @click="deleteFromGallery($event)"
                            :id="image.id"
                        />
                    </div>
                </div>
                <p class="p-left-align" v-else>
                    {{ user?.username }} has no photos in their Gallery
                </p>
                <div
                    class="gallery-image-interactive"
                    v-if="$store.state.sessionUser?.id == user?.id"
                >
                    <div class="preview-container" v-if="imageURL.length > 0">
                        <img
                            class="preview"
                            :src="imageURL"
                            alt="User uploaded image"
                        />
                    </div>
                    <div v-if="showImageInput" class="image-input">
                        <input
                            type="file"
                            accept="image/*"
                            @change="setImage($event)"
                            id="file-input"
                        />
                        <button
                            id="image-upload-button"
                            @click="uploadImage($event, this.image)"
                        >
                            {{ this.imageStatus }}
                        </button>
                    </div>
                    <button
                        id="gallery-add-button"
                        @click="addToGallery"
                        v-if="imageURL"
                    >
                        Add Image to Gallery
                    </button>
                    <button
                        id="image-upload-button"
                        v-if="!showImageInput"
                        @click="toggleShowImageInput"
                    >
                        Add to Gallery
                    </button>
                    <button v-else @click="toggleShowImageInput">Cancel</button>
                </div>
                <!-- This section can potentially be refactored using an array and using conditional classes to wrap rows/grid -->
            </div>
        </div>
        <div class="user-notebook">
            <div class="notebook-section">
                <p class="header">{{ user?.username }}'s Notebook</p>
                <div class="stats">
                    <router-link
                        v-if="usersProjects?.length == 1"
                        :to="`/users/${user?.id}/projects`"
                        >{{ usersProjects?.length }} project</router-link
                    >
                    <router-link v-else :to="`/users/${user?.id}/projects`"
                        >{{ usersProjects?.length }} projects</router-link
                    >
                    <router-link :to="`/users/${user?.id}/stash`"
                        >{{ usersStash?.length }} stashed</router-link
                    >
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                </div>
            </div>
            <!-- Possibly notebooks and summaries by craft -->
            <!-- Images could link to the project page -->
            <!-- SPINNING -->
            <div class="notebook-section" v-if="spinningProjects?.length">
                <p class="header">Spinning Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${user?.id}/projects/spinning`"
                    >{{ spinningProjects?.length }} projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in spinningProjects.slice(0, 3)"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                            @click="redirectToProject(project.id)"
                        />
                        <img
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                        />
                    </span>
                </div>
            </div>
            <!-- WEAVING -->
            <div class="notebook-section" v-if="weavingProjects?.length">
                <p class="header">Weaving Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${user?.id}/projects/weaving`"
                    >{{ weavingProjects?.length }} projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in weavingProjects.slice(0, 3)"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                            @click="redirectToProject(project.id)"
                        />
                        <img
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                        />
                    </span>
                </div>
            </div>
            <!-- KNITTING -->
            <div class="notebook-section" v-if="knittingProjects?.length">
                <p class="header">Knitting Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${user?.id}/projects/knitting`"
                    >{{ knittingProjects?.length }} projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in knittingProjects.slice(0, 3)"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                        />
                        <img
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                        />
                    </span>
                </div>
            </div>
            <!-- CROCHETING -->
            <div class="notebook-section" v-if="crochetingProjects?.length">
                <p class="header">Crocheting Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${user?.id}/projects/crocheting`"
                    >{{ crochetingProjects?.length }} projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in crochetingProjects.slice(0, 3)"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                        />
                        <img
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                        />
                    </span>
                </div>
            </div>
            <!-- SEWING -->
            <div class="notebook-section" v-if="sewingProjects?.length">
                <p class="header">Sewing Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${user?.id}/projects/sewing`"
                    >{{ sewingProjects?.length }} projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in sewingProjects.slice(0, 3)"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                            @click="redirectToProject(project.id)"
                        />
                        <img
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                        />
                    </span>
                </div>
            </div>
            <!-- EMBROIDERY -->
            <div class="notebook-section" v-if="embroideryProjects?.length">
                <p class="header">Embroidery Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${user?.id}/projects/embroidery`"
                    >{{ embroideryProjects?.length }} projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in embroideryProjects.slice(0, 3)"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                            @click="redirectToProject(project.id)"
                        />
                        <img
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                        />
                    </span>
                </div>
            </div>
            <!-- TOOLBOX -->
            <div class="notebook-section">
                <p class="header">
                    <router-link
                        class="router-link-light"
                        :to="`/users/${user?.id}/toolbox`"
                        >{{ user?.username }}'s Toolbox</router-link
                    >
                </p>
                <div v-if="usersTools?.length > 0">
                    <p class="tools-count">
                        <router-link
                            class="router-link-p"
                            :to="`/users/${user?.id}/toolbox`"
                            >{{ usersTools?.length }} Tools
                        </router-link>
                    </p>
                    <div class="stats">
                        <div class="tool-stat" v-if="spinningTools?.length">
                            <p>{{ spinningTools.length }}</p>
                            <p>Spinning Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Spinning Tools</p>
                        </div>
                        <div class="tool-stat" v-if="weavingTools?.length">
                            <p>{{ weavingTools.length }}</p>
                            <p>Weaving Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Weaving Tools</p>
                        </div>
                        <div class="tool-stat" v-if="knittingTools?.length">
                            <p>{{ knittingTools.length }}</p>
                            <p>Knitting Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Knitting Tools</p>
                        </div>
                        <div class="tool-stat" v-if="crochetingTools?.length">
                            <p>{{ crochetingTools.length }}</p>
                            <p>Crocheting Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Crocheting Tools</p>
                        </div>
                        <div class="tool-stat" v-if="sewingTools?.length">
                            <p>{{ sewingTools.length }}</p>
                            <p>Sewing Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Sewing Tools</p>
                        </div>
                        <div class="tool-stat" v-if="embroideryTools?.length">
                            <p>{{ embroideryTools.length }}</p>
                            <p>Embroidery Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Embroidery Tools</p>
                        </div>
                    </div>
                </div>
                <div v-else>
                    <p>{{ user?.username }} has no tools!</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "User",
    mounted() {
        if (!this.$store.state.sessionUser?.id) {
            this.$router.push("/login");
        }
        const userData = loadUser(this.$route.params.id).then((data) => {
            if (data) {
                this.user = data;
            } else {
                this.$router.push("/404");
            }
        });
        const galleryData = loadUsersPhotos(this.$route.params.id).then(
            (galleryData) => {
                if (galleryData) {
                    this.usersPhotos = Object.values(galleryData)[0];
                }
            }
        );
        const stashData = loadUsersStash(this.$route.params.id).then(
            (stashData) => {
                if (stashData) {
                    this.usersStash = Object.values(stashData)[0];
                }
            }
        );
        const toolsData = loadUsersTools(this.$route.params.id).then(
            (toolsData) => {
                if (toolsData) {
                    if (Array.isArray(toolsData)) {
                        this.usersTools = toolsData;
                    } else {
                        this.usersTools = Object.values(toolsData)[0];
                    }
                    const spinningArr = [];
                    const weavingArr = [];
                    const knittingArr = [];
                    const crochetingArr = [];
                    const sewingArr = [];
                    const embroideryArr = [];
                    Object.values(toolsData)[0].forEach((tool) => {
                        if (tool.forSpinning) {
                            spinningArr.push(tool);
                        }
                        if (tool.forWeaving) {
                            weavingArr.push(tool);
                        }
                        if (tool.forKnitting) {
                            knittingArr.push(tool);
                        }
                        if (tool.forCrocheting) {
                            crochetingArr.push(tool);
                        }
                        if (tool.forSewing) {
                            sewingArr.push(tool);
                        }
                        if (tool.forEmbroidery) {
                            embroideryArr.push(tool);
                        }
                    });
                    this.spinningTools = spinningArr;
                    this.weavingTools = weavingArr;
                    this.knittingTools = knittingArr;
                    this.crochetingTools = crochetingArr;
                    this.sewingTools = sewingArr;
                    this.embroideryTools = embroideryArr;
                }
            }
        );
        const projectsData = loadUsersProjects(this.$route.params.id).then(
            (projectsData) => {
                if (projectsData) {
                    if (Array.isArray(projectsData)) {
                        this.usersProjects = projectsData;
                    } else {
                        this.usersProjects = Object.values(projectsData)[0];
                    }
                    const spinningArr = [];
                    const weavingArr = [];
                    const knittingArr = [];
                    const crochetingArr = [];
                    const sewingArr = [];
                    const embroideryArr = [];
                    Object.values(projectsData)[0].forEach((project) => {
                        if (project.craftTypes?.includes("spinning")) {
                            spinningArr.push(project);
                        }
                        if (project.craftTypes?.includes("weaving")) {
                            weavingArr.push(project);
                        }
                        if (project.craftTypes?.includes("knitting")) {
                            knittingArr.push(project);
                        }
                        if (project.craftTypes?.includes("crocheting")) {
                            crochetingArr.push(project);
                        }
                        if (project.craftTypes?.includes("sewing")) {
                            sewingArr.push(project);
                        }
                        if (project.craftTypes?.includes("embroidery")) {
                            embroideryArr.push(project);
                        }
                    });
                    this.spinningProjects = spinningArr;
                    this.weavingProjects = weavingArr;
                    this.knittingProjects = knittingArr;
                    this.crochetingProjects = crochetingArr;
                    this.sewingProjects = sewingArr;
                    this.embroideryProjects = embroideryArr;
                }
            }
        );
    },
    data() {
        return {
            user: null,
            usersPhotos: null,
            usersStash: [],

            usersTools: [],
            spinningTools: [],
            weavingTools: [],
            knittingTools: [],
            crochetingTools: [],
            sewingTools: [],
            embroideryTools: [],

            usersProjects: [],
            spinningProjects: [],
            weavingProjects: [],
            knittingProjects: [],
            crochetingProjects: [],
            sewingProjects: [],
            embroideryProjects: [],

            showImageInput: false,
            image: null,
            imageURL: "",
            imageStatus: "Upload",
            stashData: null,
        };
    },
    methods: {
        edit: function () {
            this.$router.push(`/users/edit`);
        },
        toggleShowImageInput: function () {
            this.showImageInput = !this.showImageInput;
        },
        setImage($event) {
            this.image = $event.target.files[0];
        },
        async uploadImage($event, image) {
            $event.preventDefault();
            this.imageStatus = "Loading...";
            const formData = new FormData();
            formData.append("image", image);

            const res = await fetch("/api/images", {
                method: "POST",
                body: formData,
            });

            if (res.ok) {
                let data = await res.json();
                this.imageURL = data.url;
                this.imageStatus = "Uploaded!";
            } else {
                this.imageStatus = "Image not found / Invalid image!";
            }
        },
        async addToGallery($event) {
            $event.preventDefault();

            const image = {
                user_id: this.$store.state.sessionUser.id,
                image_url: this.imageURL,
            };
            const response = await fetch("/api/gallery/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(image),
            });
            if (response.ok) {
                const data = await response.json();
                const galleryData = loadUsersPhotos(this.$route.params.id).then(
                    (galleryData) => {
                        if (galleryData) {
                            this.$store.commit("setUsersPhotos", galleryData);
                        }
                    }
                );
                this.showImageInput = false;
                this.image = null;
                this.imageURL = "";
                this.imageStatus = "Upload";
            }
        },
        async deleteFromGallery($event) {
            $event.preventDefault();

            const response = await fetch("/api/gallery/", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: parseInt($event.target.id),
                }),
            });
            if (response.ok) {
                const data = await response.json();
                const galleryData = loadUsersPhotos(this.$route.params.id).then(
                    (galleryData) => {
                        if (galleryData) {
                            this.$store.commit("setUsersPhotos", galleryData);
                        }
                    }
                );
            }
        },
        redirectToProject(id) {
            this.$router.push(`/projects/${id}`);
        },
    },
};

const loadUser = async (userId) => {
    const response = await fetch(`/api/users/${userId}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        return false;
    }
};

const loadUsersPhotos = async (userId) => {
    const response = await fetch(`/api/gallery/users/${userId}`);
    if (response.ok) {
        const galleryData = await response.json();
        return galleryData;
    } else {
        return false;
    }
};

const loadUsersStash = async (userId) => {
    const response = await fetch(`/api/stash/users/${userId}`);
    if (response.ok) {
        const stashData = await response.json();
        return stashData;
    } else {
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

const loadUsersProjects = async (userId) => {
    const response = await fetch(`/api/projects/users/${userId}`);
    if (response.ok) {
        const projectsData = await response.json();
        return projectsData;
    } else {
        return false;
    }
};
</script>

<style scoped>
a {
    text-decoration: none;
    color: var(--color-shadow);
    align-self: center;
}

a:hover {
    font-weight: bold;
}

.user-body {
    padding-top: 60px;
    padding-bottom: 32px;
    padding-left: 8%;
    padding-right: 8%;
    display: grid;
    grid-template-columns: 120px 1fr 300px;
    column-gap: 8%;
}

.user-left {
    display: flex;
    flex-direction: column;
    row-gap: 12px;
    text-align: center;
}

.user-left > h3 {
    margin-top: 0px;
}

.user-left > img {
    height: 120px;
    width: 120px;
    object-fit: cover;
    border-radius: 4px;
    border: 1px solid var(--color-shadow);
}

.user-left > button {
    border: 1px solid var(--color-shadow);
    background-color: var(--color-primary-contrast);
    border-radius: 4px;
    color: white;
    box-shadow: 2px 2px 2px var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
}

.user-left > button:hover {
    cursor: pointer;
}

.user-left > button:active {
    box-shadow: 3px 3px 2px var(--color-shadow);
}
.social-container {
    display: grid;
    grid-template-columns: 32px 1fr;
    column-gap: 20px;
}

.icon {
    height: 32px;
    width: 32px;
    align-self: center;
}

.social-text {
    font-size: 13px;
    text-align: left;
    align-self: center;
    display: grid;
    grid-template-rows: 1fr 1fr;
}

.social-text > p {
    margin: 0px;
    align-self: center;
}

.social-text > a {
    color: var(--color-primary-contrast);
    font-size: 14px;
}

.crafts-container {
    margin-top: 8px;
    margin-bottom: 8px;
}

.crafts-container > .header {
    font-size: 15px;
    font-weight: bold;
    margin-bottom: 8px;
}

.crafts-container > .craft-button {
    width: 100px;
    background-color: var(--color-primary-contrast);
    margin-left: auto;
    margin-right: auto;
    margin-top: 4px;
    margin-bottom: 4px;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
    padding-top: 3px;
    padding-bottom: 3px;
    color: white;
    box-shadow: 2px 2px 2px var(--color-shadow);
    letter-spacing: 1px;
    font-size: 13px;
    font-family: "Open Sans", sans-serif;
}

.user-main {
    min-width: 0px;
}

.user-text {
    display: grid;
    grid-template-columns: 25% calc(75% - 20px);
    column-gap: 14px;
    row-gap: 20px;
    text-align: justify;
    font-size: 14px;
    align-content: flex-start;
    min-width: 0px;
}

.user-text-label {
    text-align: left;
}

.user-gallery-container {
    width: 100%;
}

.user-gallery-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 0px;
    margin-bottom: -40px;
    margin-top: 16px;
}

.user-gallery-header > h4 {
    padding: 0px;
}

.gallery-image-interactive {
    display: flex;
    flex-direction: column;
    margin-top: 24px;
    column-gap: 12px;
    align-items: center;
    width: 100%;
}

.gallery-image-interactive > button {
    border: 1px solid var(--color-shadow);
    background-color: var(--color-primary-contrast);
    border-radius: 4px;
    color: white;
    box-shadow: 2px 2px 2px var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    height: 34px;
    margin-top: 6px;
    margin-bottom: 6px;
}

.gallery-image-interactive > button:hover {
    cursor: pointer;
}

.gallery-image-interactive > button:active {
    box-shadow: 3px 3px 2px var(--color-shadow);
}

.image-input {
    margin-top: 6px;
    margin-bottom: 6px;
}

#gallery-add-button {
    border: 1px solid var(--color-shadow);
    background-color: var(--color-primary-contrast);
    border-radius: 4px;
    color: white;
    box-shadow: 2px 2px 2px var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    height: 34px;
    margin-top: 18px;
    margin-bottom: 6px;
}

#gallery-add-button:hover {
    cursor: pointer;
}

#gallery-add-button:active {
    box-shadow: 3px 3px 2px var(--color-shadow);
}

.preview-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    margin-top: 12px;
    margin-bottom: 6px;
}

.preview {
    width: 140px;
    height: 140px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.user-gallery {
    margin-top: 48px;
    display: grid;
    justify-content: space-between;
    grid-template-columns: repeat(auto-fill, 140px);
    grid-gap: 12px;
}

.gallery-image-container {
    position: relative;
    width: 140px;
    height: 140px;
}

.gallery-image-container > img {
    width: 140px;
    height: 140px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.gallery-image-container > i {
    position: absolute;
    left: 4px;
    top: 4px;
    color: var(--color-nav);
    text-shadow: 0px 0px 3px var(--color-shadow);
}

.gallery-image-container > i:hover {
    cursor: pointer;
}

.notebook-section {
    width: 300px;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
    box-shadow: 2px 2px 2px var(--color-shadow);
    margin-bottom: 24px;
}

.notebook-section > .header {
    width: 100%;
    background-color: var(--color-primary-contrast);
    margin: 0px;
    padding-top: 8px;
    padding-bottom: 8px;
    color: white;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
}

.notebook-section > p {
    font-size: 14px;
    margin-top: 12px;
    margin-bottom: 8px;
}

.stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    font-size: 14px;
    margin-top: 6px;
    margin-bottom: 6px;
}

.stats > p {
    margin-top: 4px;
    margin-bottom: 4px;
}

.notebook-section > .tiny-gallery {
    padding-top: 6px;
    padding-bottom: 12px;
    padding-left: 14px;
    padding-right: 14px;
    display: grid;
    grid-template-columns: repeat(auto-fill, 84px);
    justify-content: space-between;
}

.notebook-section > .tiny-gallery > span > img {
    width: 80px;
    height: 80px;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.notebook-section > .tiny-gallery > span > img:hover {
    cursor: pointer;
}

.notebook-section > .tiny-gallery > span > img:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.pronouns-container {
    margin-bottom: 8px;
    margin-top: -20px;
}

.pronouns {
    margin: 0px;
    font-size: 13px;
}

.tools-count {
    font-size: 12px;
}

.tool-stat {
    margin-bottom: 12px;
}

.tool-stat > p {
    margin-top: 0px;
    margin-bottom: 0px;
    font-size: 13px;
}

.router-link-light {
    color: white;
    text-decoration: none;
}

.router-link-p {
    color: var(--color-shadow);
    text-decoration: none;
}

.router-link-p:active {
    font-weight: bold;
}

.router-link-small {
    font-size: 14px;
}

.grayed {
    color: #7597aa;
}

.divider {
    border-top: 1px solid var(--color-shadow);
    margin-top: 16px;
    margin-bottom: 16px;
    padding: 0px;
}

.p-left-align {
    text-align: left;
    margin-top: 32px;
}
</style>
