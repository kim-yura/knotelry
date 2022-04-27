<template>
    <div class="edit-user-body">
        <form class="edit-user-form" @submit.prevent="submit">
            <div class="form-element">
                <div />
                <h2>Editing User Profile</h2>
            </div>
            <div class="form-element" v-if="this.imageURL?.length > 0">
                <div />
                <img
                    class="tool-image"
                    :src="this.imageURL"
                    alt="User uploaded image"
                />
            </div>
            <div class="form-element">
                <label for="image">Upload Image:</label>
                <div class="image-input">
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
            </div>
            <div class="form-element">
                <label for="bio">Bio:</label>
                <textarea
                    name="bio"
                    placeholder="Tell us about yourself!"
                    v-model="bio"
                />
            </div>
            <div class="form-element">
                <label for="craftingJourney">Crafting Journey:</label>
                <textarea
                    name="craftingJourney"
                    placeholder="Tell us about your crafting journey!"
                    v-model="craftingJourney"
                />
            </div>
            <div class="form-element">
                <label for="roles">Roles:</label>
                <input
                    type="text"
                    name="roles"
                    placeholder="Tell us about your roles in the crafting community"
                    v-model="roles"
                />
            </div>
            <div class="form-element">
                <label for="pronouns">Pronouns:</label>
                <div class="pronouns-container">
                    <button
                        v-if="pronounsShe"
                        @click="toggleShe"
                        class="selected"
                    >
                        she/her/hers
                    </button>
                    <button v-else @click="toggleShe">she/her/hers</button>
                    <button
                        v-if="pronounsHe"
                        @click="toggleHe"
                        class="selected"
                    >
                        he/him/his
                    </button>
                    <button v-else @click="toggleHe">he/him/his</button>
                    <button
                        v-if="pronounsThey"
                        @click="toggleThey"
                        class="selected"
                    >
                        they/them/theirs
                    </button>
                    <button v-else @click="toggleThey">they/them/theirs</button>
                </div>
            </div>
            <div class="form-element">
                <label for="pronounsCustom">Custom pronouns:</label>
                <input
                    type="text"
                    name="pronounsCustom"
                    placeholder="Enter comma-separated custom pronouns"
                    v-model="pronounsCustom"
                />
            </div>
            <div class="form-element">
                <label for="instagram">Instagram:</label>
                <input
                    type="text"
                    name="instagram"
                    placeholder="Enter Instagram account name"
                    v-model="instagram"
                />
            </div>
            <div class="form-element">
                <label for="twitter">Twitter:</label>
                <input
                    type="text"
                    name="twitter"
                    placeholder="Enter Twitter handle name"
                    v-model="twitter"
                />
            </div>
            <div class="form-element">
                <label for="kofi">Ko-fi:</label>
                <input
                    type="text"
                    name="kofi"
                    placeholder="Enter Ko-fi account name"
                    v-model="kofi"
                />
            </div>
            <div class="form-element">
                <label for="website">Website:</label>
                <input
                    type="text"
                    name="website"
                    placeholder="Enter website URL"
                    v-model="website"
                />
            </div>
            <div class="form-element">
                <label for="crafts">Crafts:</label>
                <div class="crafts-container">
                    <button
                        v-if="isSpinner"
                        @click="toggleSpinner"
                        class="selected"
                    >
                        Spinning
                    </button>
                    <button v-else @click="toggleSpinner">Spinning</button>
                    <button
                        v-if="isWeaver"
                        @click="toggleWeaver"
                        class="selected"
                    >
                        Weaving
                    </button>
                    <button v-else @click="toggleWeaver">Weaving</button>
                    <button
                        v-if="isKnitter"
                        @click="toggleKnitter"
                        class="selected"
                    >
                        Knitting
                    </button>
                    <button v-else @click="toggleKnitter">Knitting</button>
                    <button
                        v-if="isCrocheter"
                        @click="toggleCrocheter"
                        class="selected"
                    >
                        Crocheting
                    </button>
                    <button v-else @click="toggleCrocheter">Crocheting</button>
                    <button
                        v-if="isSewist"
                        @click="toggleSewist"
                        class="selected"
                    >
                        Sewing
                    </button>
                    <button v-else @click="toggleSewist">Sewing</button>
                    <button
                        v-if="isEmbroiderer"
                        @click="toggleEmbroiderer"
                        class="selected"
                    >
                        Embroidery
                    </button>
                    <button v-else @click="toggleEmbroiderer">
                        Embroidery
                    </button>
                    <!-- MORE CRAFTS GO HERE -->
                </div>
            </div>
            <div class="form-element">
                <div />
                <div class="option-buttons">
                    <button id="submit" type="submit">Submit Changes</button>
                    <p class="option-button" id="cancel-button" @click="cancel">
                        Cancel Edit
                    </p>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "UserEdit",
    mounted() {
        const sessionUser = this.$store.state.sessionUser;
        if (sessionUser === null) {
            this.$router.push("/404");
        }
    },
    data() {
        return {
            bio: this.$store.state.sessionUser.bio,
            craftingJourney: this.$store.state.sessionUser.crafting_journey,
            roles: this.$store.state.sessionUser.roles,
            pronounsShe: this.$store.state.sessionUser.pronouns_she,
            pronounsHe: this.$store.state.sessionUser.pronouns_he,
            pronounsThey: this.$store.state.sessionUser.pronouns_they,
            pronounsCustom: this.$store.state.sessionUser.pronouns_custom,

            instagram: this.$store.state.sessionUser.instagram,
            twitter: this.$store.state.sessionUser.twitter,
            kofi: this.$store.state.sessionUser.kofi,
            website: this.$store.state.sessionUser.website,

            isSpinner: this.$store.state.sessionUser.is_spinner,
            isWeaver: this.$store.state.sessionUser.is_weaver,
            isKnitter: this.$store.state.sessionUser.is_knitter,
            isCrocheter: this.$store.state.sessionUser.is_crocheter,
            isSewist: this.$store.state.sessionUser.is_sewist,
            isEmbroiderer: this.$store.state.sessionUser.is_embroiderer,

            image: null,
            imageURL: this.$store.state.sessionUser.profile_pic_url,
            imageStatus: "Upload",
        };
    },
    methods: {
        toggleShe: function () {
            this.pronounsShe = !this.pronounsShe;
        },
        toggleHe: function () {
            this.pronounsHe = !this.pronounsHe;
        },
        toggleThey: function () {
            this.pronounsThey = !this.pronounsThey;
        },
        toggleSpinner: function () {
            this.isSpinner = !this.isSpinner;
        },
        toggleWeaver: function () {
            this.isWeaver = !this.isWeaver;
        },
        toggleKnitter: function () {
            this.isKnitter = !this.isKnitter;
        },
        toggleCrocheter: function () {
            this.isCrocheter = !this.isCrocheter;
        },
        toggleSewist: function () {
            this.isSewist = !this.isSewist;
        },
        toggleEmbroiderer: function () {
            this.isEmbroiderer = !this.isEmbroiderer;
        },
        async submit() {
            const editedUser = {
                id: this.$store.state.sessionUser.id,
                bio: this.bio,
                craftingJourney: this.craftingJourney,
                roles: this.roles,
                profilePicURL: this.imageURL,
                pronounsShe: this.pronounsShe,
                pronounsHe: this.pronounsHe,
                pronounsThey: this.pronounsThey,
                pronounsCustom: this.pronounsCustom,
                instagram: this.instagram,
                twitter: this.twitter,
                kofi: this.kofi,
                website: this.website,
                isSpinner: this.isSpinner,
                isWeaver: this.isWeaver,
                isKnitter: this.isKnitter,
                isCrocheter: this.isCrocheter,
                isSewist: this.isSewist,
                isEmbroiderer: this.isEmbroiderer,
            };
            const response = await fetch("/api/users/", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(editedUser),
            });
            if (response.ok) {
                const data = await response.json();
                this.$store.commit("logIn", data);
                this.$router.push(`/users/${data.id}`);
            }
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
        cancel() {
            this.$router.push(`/users/${this.$store.state.sessionUser.id}`);
        },
    },
    mutations: {
        ...mapMutations,
    },
};
</script>

<style scoped>
.edit-user-body {
    margin-left: 25%;
    margin-right: 25%;
    margin-top: 48px;
    margin-bottom: 48px;
}

.edit-user-form {
    display: flex;
    flex-direction: column;
    font-family: "Open Sans", sans-serif;
}

.form-element {
    display: grid;
    grid-template-columns: 150px 1fr;
    column-gap: 16px;
    margin-bottom: 6px;
}

label {
    text-align: justify;
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
}

textarea {
    font-size: 14px;
    font-family: "Open Sans", sans-serif;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
    padding-top: 6px;
    padding-bottom: 6px;
    padding-left: 10px;
    padding-right: 10px;
    resize: vertical;
    min-height: 100px;
}

.pronouns-container {
    display: flex;
    flex-wrap: wrap;
    row-gap: 6px;
    align-items: center;
    justify-content: space-between;
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
}

button:hover {
    cursor: pointer;
}

.selected {
    background-color: var(--color-primary-contrast);
    color: white;
}

button:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.crafts-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    row-gap: 6px;
}

#submit {
    width: 100%;
    font-size: 16px;
    margin-top: 6px;
    letter-spacing: 2px;
    color: white;
    background-color: var(--color-primary-contrast);
    margin-bottom: 48px;
}

h2 {
    margin-bottom: 14px;
}

.image-input {
    width: 100%;
}

.image-input > input {
    width: 100%;
    border: none;
}

.tool-image {
    width: 250px;
    margin-left: auto;
    margin-right: auto;
    height: auto;
    object-fit: contain;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
}

#image-upload-button {
    width: 100%;
}

#file-upload-button {
    font-family: "Open Sans", sans-serif;
}

.option-buttons {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 4px;
}

.option-button {
    font-size: 16px;
    margin-top: 6px;
    color: white;
    background-color: var(--color-primary-contrast);
    margin-bottom: 48px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1.5px;
    padding-top: 4px;
    padding-bottom: 4px;
    border-radius: 4px;
    border: 1px solid var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
}

.option-button:hover {
    cursor: pointer;
}

.option-button:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

#cancel-button {
    color: var(--color-primary-contrast);
    background-color: white;
}
</style>
