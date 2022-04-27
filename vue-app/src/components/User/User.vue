<template>
    <div v-if="$store.state.selectedUser?.id" class="user-body">
        <div class="user-left">
            <h3>{{ $store.state.selectedUser?.username }}</h3>
            <div class="pronouns-container">
                <p
                    class="pronouns"
                    v-if="$store.state.selectedUser.pronouns_she"
                >
                    she/her/hers
                </p>
                <p
                    class="pronouns"
                    v-if="$store.state.selectedUser.pronouns_he"
                >
                    he/him/his
                </p>
                <p
                    class="pronouns"
                    v-if="$store.state.selectedUser.pronouns_they"
                >
                    they/them/theirs
                </p>
                <span
                    class="pronouns"
                    v-if="$store.state.selectedUser.pronouns_custom?.length"
                >
                    <p
                        v-for="pronoun in $store.state.selectedUser.pronouns_custom.split(
                            ','
                        )"
                        :key="pronoun"
                        class="pronouns"
                    >
                        {{ pronoun }}
                    </p>
                </span>
            </div>
            <button
                v-if="
                    $store.state.sessionUser?.id ==
                    $store.state.selectedUser?.id
                "
                @click="edit"
            >
                Edit Profile
            </button>
            <img
                v-if="$store.state.selectedUser"
                :src="$store.state.selectedUser.profile_pic_url"
                class="user-profile"
                alt="User profile"
            />
            <!-- SOCIAL LINKS -->
            <div
                class="social-container"
                v-if="$store.state.selectedUser?.instagram"
            >
                <img
                    src="https://upload.wikimedia.org/wikipedia/commons/5/58/Instagram-Icon.png"
                    class="icon"
                    alt="Instagram icon"
                />
                <div class="social-text">
                    <p>Instagram:</p>
                    <a
                        v-bind:href="
                            'https://www.instagram.com/' +
                            $store.state.selectedUser.instagram
                        "
                        target="_blank"
                        >{{ $store.state.selectedUser.instagram }}
                    </a>
                </div>
            </div>
            <div
                class="social-container"
                v-if="$store.state.selectedUser?.twitter"
            >
                <img
                    src="https://upload.wikimedia.org/wikipedia/commons/4/4f/Twitter-logo.svg"
                    class="icon"
                    alt="Twitter icon"
                />
                <div class="social-text">
                    <p>Twitter:</p>
                    <a
                        v-bind:href="
                            'https://twitter.com/' +
                            $store.state.selectedUser.twitter
                        "
                        target="_blank"
                        >{{ $store.state.selectedUser.twitter }}
                    </a>
                </div>
            </div>
            <div
                class="social-container"
                v-if="$store.state.selectedUser?.kofi"
            >
                <img
                    src="https://uploads-ssl.webflow.com/5c14e387dab576fe667689cf/61e1116779fc0a9bd5bdbcc7_Frame%206.png"
                    class="icon"
                    alt="Ko-fi icon"
                />
                <div class="social-text">
                    <p>Ko-fi:</p>
                    <a
                        v-bind:href="
                            'https://ko-fi.com/' +
                            $store.state.selectedUser.kofi
                        "
                        target="_blank"
                        >{{ $store.state.selectedUser.kofi }}
                    </a>
                </div>
            </div>
            <div
                class="social-container"
                v-if="$store.state.selectedUser?.website"
            >
                <img
                    src="https://w7.pngwing.com/pngs/549/715/png-transparent-web-development-logo-website-web-design-symmetry-internet-thumbnail.png"
                    class="icon"
                    alt="Web icon"
                />
                <div class="social-text">
                    <p>Website:</p>
                    <a
                        v-bind:href="
                            'https://' + $store.state.selectedUser.website
                        "
                        target="_blank"
                        >{{ $store.state.selectedUser.website }}
                    </a>
                </div>
            </div>

            <!-- Toggle query for crafts -->
            <div class="crafts-container">
                <p class="header">
                    {{ $store.state.selectedUser?.username }}'s Crafts
                </p>
                <!-- Each button can maybe redirect to that user's craft notebook -->
                <button
                    v-if="$store.state.selectedUser?.is_spinner"
                    class="craft-button"
                >
                    spinning
                </button>
                <button
                    v-if="$store.state.selectedUser?.is_weaver"
                    class="craft-button"
                >
                    weaving
                </button>
                <button
                    v-if="$store.state.selectedUser?.is_knitter"
                    class="craft-button"
                >
                    knitting
                </button>
                <button
                    v-if="$store.state.selectedUser?.is_crocheter"
                    class="craft-button"
                >
                    crocheting
                </button>
                <button
                    v-if="$store.state.selectedUser?.is_sewist"
                    class="craft-button"
                >
                    sewing
                </button>
                <button
                    v-if="$store.state.selectedUser?.is_embroiderer"
                    class="craft-button"
                >
                    embroidery
                </button>
            </div>

            <div class="user-text-label">
                <img v-if="$store.state.selectedUser?.twitter" />
            </div>
        </div>
        <div class="user-main">
            <div class="user-text">
                <div class="user-text-label">Bio:</div>
                <div
                    class="user-text-content"
                    v-if="$store.state.selectedUser?.bio?.length"
                >
                    {{ $store.state.selectedUser.bio }}
                </div>
                <div class="user-text-content" v-else>—</div>
                <div class="user-text-label">Crafting Journey:</div>
                <div
                    class="user-text-content"
                    v-if="$store.state.selectedUser?.crafting_journey?.length"
                >
                    {{ $store.state.selectedUser.crafting_journey }}
                </div>
                <div class="text-content" v-else>—</div>
                <div class="user-text-label">Roles:</div>
                <div
                    class="user-text-content"
                    v-if="$store.state.selectedUser?.roles?.length"
                >
                    {{ $store.state.selectedUser.roles }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="divider" />
            <div class="user-gallery-container">
                <div class="user-gallery-header">
                    <h4>{{ $store.state.selectedUser?.username }}'s Gallery</h4>
                </div>
                <div
                    class="user-gallery"
                    v-if="$store.state.usersPhotos.length > 0"
                >
                    <div
                        v-for="image in $store.state.usersPhotos"
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
                            v-if="
                                $store.state.sessionUser?.id ==
                                $store.state.selectedUser?.id
                            "
                            @click="deleteFromGallery($event)"
                            :id="image.id"
                        />
                    </div>
                </div>
                <div class="user-gallery" v-else>
                    <p>
                        {{ $store.state.selectedUser?.username }} has no photos
                        in their Gallery
                    </p>
                </div>
                <div
                    class="gallery-image-interactive"
                    v-if="
                        $store.state.sessionUser?.id ==
                        $store.state.selectedUser?.id
                    "
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
                <p class="header">
                    {{ $store.state.selectedUser?.username }}'s Notebook
                </p>
                <div class="stats">
                    <router-link
                        v-if="$store.state.usersProjects?.length == 1"
                        :to="`/users/${$store.state.selectedUser?.id}/projects`"
                        >{{
                            $store.state.usersProjects?.length
                        }}
                        project</router-link
                    >
                    <router-link
                        v-else
                        :to="`/users/${$store.state.selectedUser?.id}/projects`"
                        >{{
                            $store.state.usersProjects?.length
                        }}
                        projects</router-link
                    >
                    <router-link
                        :to="`/users/${$store.state.selectedUser?.id}/stash`"
                        >{{
                            $store.state.usersStash?.length
                        }}
                        stashed</router-link
                    >
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                </div>
            </div>
            <!-- TOOLBOX -->
            <div class="notebook-section">
                <p class="header">
                    <router-link
                        class="router-link-light"
                        :to="`/users/${$store.state.selectedUser?.id}/toolbox`"
                        >{{ $store.state.selectedUser?.username }}'s
                        Toolbox</router-link
                    >
                </p>
                <div v-if="$store.state.usersTools?.length > 0">
                    <p class="tools-count">
                        <router-link
                            class="router-link-p"
                            :to="`/users/${$store.state.selectedUser?.id}/toolbox`"
                            >{{ $store.state.usersTools.length }} Tools
                        </router-link>
                    </p>
                    <div class="stats">
                        <div
                            class="tool-stat"
                            v-if="$store.state.spinningTools?.length"
                        >
                            <p>{{ $store.state.spinningTools.length }}</p>
                            <p>Spinning Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Spinning Tools</p>
                        </div>
                        <div
                            class="tool-stat"
                            v-if="$store.state.weavingTools?.length"
                        >
                            <p>{{ $store.state.weavingTools.length }}</p>
                            <p>Weaving Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Weaving Tools</p>
                        </div>
                        <div
                            class="tool-stat"
                            v-if="$store.state.knittingTools?.length"
                        >
                            <p>{{ $store.state.knittingTools.length }}</p>
                            <p>Knitting Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Knitting Tools</p>
                        </div>
                        <div
                            class="tool-stat"
                            v-if="$store.state.crochetingTools?.length"
                        >
                            <p>{{ $store.state.crochetingTools.length }}</p>
                            <p>Crocheting Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Crocheting Tools</p>
                        </div>
                        <div
                            class="tool-stat"
                            v-if="$store.state.sewingTools?.length"
                        >
                            <p>{{ $store.state.sewingTools.length }}</p>
                            <p>Sewing Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Sewing Tools</p>
                        </div>
                        <div
                            class="tool-stat"
                            v-if="$store.state.embroideryTools?.length"
                        >
                            <p>{{ $store.state.embroideryTools.length }}</p>
                            <p>Embroidery Tools</p>
                        </div>
                        <div class="tool-stat grayed" v-else>
                            <p>-</p>
                            <p>Embroidery Tools</p>
                        </div>
                    </div>
                </div>
                <div v-else>
                    <p>
                        {{ $store.state.selectedUser?.username }} has no tools!
                    </p>
                </div>
            </div>
            <!-- Possibly notebooks and summaries by craft -->
            <!-- Images could link to the project page -->
            <!-- SPINNING -->
            <div
                class="notebook-section"
                v-if="$store.state.spinningProjects?.length"
            >
                <p class="header">Spinning Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${$store.state.selectedUser?.id}/projects/spinning`"
                    >{{
                        $store.state.spinningProjects?.length
                    }}
                    projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in $store.state.spinningProjects.slice(
                            0,
                            3
                        )"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                            @click="redirectToProject(project.id)"
                        />
                        <img v-else src="" alt="No image found" />
                    </span>
                </div>
            </div>
            <!-- KNITTING -->
            <div
                class="notebook-section"
                v-if="$store.state.knittingProjects?.length"
            >
                <p class="header">Knitting Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${$store.state.selectedUser?.id}/projects/knitting`"
                    >{{
                        $store.state.knittingProjects?.length
                    }}
                    projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in $store.state.knittingProjects.slice(
                            0,
                            3
                        )"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                        />
                        <img v-else src="" alt="No image found" />
                    </span>
                </div>
            </div>
            <!-- CROCHETING -->
            <div
                class="notebook-section"
                v-if="$store.state.crochetingProjects?.length"
            >
                <p class="header">Crocheting Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${$store.state.selectedUser?.id}/projects/crocheting`"
                    >{{
                        $store.state.crochetingProjects?.length
                    }}
                    projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in $store.state.crochetingProjects.slice(
                            0,
                            3
                        )"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                        />
                        <img v-else src="" alt="No image found" />
                    </span>
                </div>
            </div>
            <!-- SEWING -->
            <div
                class="notebook-section"
                v-if="$store.state.sewingProjects?.length"
            >
                <p class="header">Sewing Notebook</p>
                <router-link
                    class="router-link-small"
                    :to="`/users/${$store.state.selectedUser?.id}/projects/sewing`"
                    >{{
                        $store.state.sewingProjects?.length
                    }}
                    projects</router-link
                >
                <div class="tiny-gallery">
                    <span
                        v-for="project in $store.state.sewingProjects.slice(
                            0,
                            3
                        )"
                        :key="project.id"
                    >
                        <img
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            :key="project.id"
                            alt="User-uploaded project image"
                            @click="redirectToProject(project.id)"
                        />
                        <img v-else src="" alt="No image found" />
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "User",
    mounted() {
        this.$store.commit("clearSelectedUser");
        const data = loadUser(this.$route.params.id).then((data) => {
            if (data) {
                this.$store.commit("setSelectedUser", data);
            } else {
                this.$router.push("/404");
            }
        });
        const galleryData = loadUsersPhotos(this.$route.params.id).then(
            (galleryData) => {
                if (galleryData) {
                    this.$store.commit("setUsersPhotos", galleryData);
                }
            }
        );
        const stashData = loadUsersStash(this.$route.params.id).then(
            (stashData) => {
                if (stashData) {
                    this.$store.commit("setUsersStash", stashData);
                }
            }
        );
        const toolsData = loadUsersTools(this.$route.params.id).then(
            (toolsData) => {
                if (toolsData) {
                    this.$store.commit("setUsersTools", toolsData);
                    this.$store.commit("setUsersToolCategories", toolsData);
                }
            }
        );
        const projectsData = loadUsersProjects(this.$route.params.id).then(
            (projectsData) => {
                if (projectsData) {
                    this.$store.commit("setUsersProjects", projectsData);
                    this.$store.commit(
                        "setUsersProjectCategories",
                        projectsData
                    );
                }
            }
        );
    },
    data() {
        return {
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

const loadUsersPhotos = async (userId) => {
    const response = await fetch(`/api/gallery/users/${userId}`);
    if (response.ok) {
        const galleryData = await response.json();
        return galleryData;
    } else {
        const galleryData = false;
        return false;
    }
};

const loadUsersStash = async (userId) => {
    const response = await fetch(`/api/stash/users/${userId}`);
    if (response.ok) {
        const stashData = await response.json();
        return stashData;
    } else {
        const stashData = false;
        return false;
    }
};

const loadUsersTools = async (userId) => {
    const response = await fetch(`/api/tools/users/${userId}`);
    if (response.ok) {
        const toolsData = await response.json();
        return toolsData;
    } else {
        const toolsData = false;
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
    object-fit: contain;
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
</style>
