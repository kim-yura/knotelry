<template>
    <div class="tool-form-body">
        <form class="tool-form" @submit.prevent="submit">
            <div class="form-element">
                <div />
                <h2>Creating New Tool</h2>
            </div>
            <div class="form-element" v-if="this.validationErrors.length">
                <div />
                <div class="error-container">
                    <p
                        class="error"
                        v-for="error in this.validationErrors"
                        :key="error"
                    >
                        {{ error }}
                    </p>
                </div>
            </div>
            <div class="form-element">
                <label for="title">Title:</label>
                <input
                    type="text"
                    placeholder="Enter a title for your tool"
                    v-model="title"
                />
            </div>
            <div class="form-element" v-if="this.imageURL.length > 0">
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
                <label for="description">Description:</label>
                <textarea
                    placeholder="Enter descriptions and notes for your tool"
                    v-model="description"
                />
            </div>
            <div class="form-element">
                <label for="acquired">Date Acquired:</label>
                <input type="date" v-model="acquired" />
            </div>
            <div class="form-element">
                <label for="status">Status:</label>
                <select v-model="status">
                    <option value=null selected disabled hidden>
                        —
                    </option>
                    <option value="inStash">In stash</option>
                    <option value="inUse">In use</option>
                    <option value="loaned">Loaned</option>
                </select>
            </div>
            <div class="form-element">
                <label for="crafts">Crafts:</label>
                <div class="crafts-container">
                    <button
                        v-bind:class="{ selected: forSpinning }"
                        @click.prevent="toggleSpinning"
                    >
                        Spinning
                    </button>
                    <button
                        v-bind:class="{ selected: forWeaving }"
                        @click.prevent="toggleWeaving"
                    >
                        Weaving
                    </button>
                    <button
                        v-bind:class="{ selected: forKnitting }"
                        @click.prevent="toggleKnitting"
                    >
                        Knitting
                    </button>
                    <button
                        v-bind:class="{ selected: forCrocheting }"
                        @click.prevent="toggleCrocheting"
                    >
                        Crocheting
                    </button>
                    <button
                        v-bind:class="{ selected: forSewing }"
                        @click.prevent="toggleSewing"
                    >
                        Sewing
                    </button>
                    <button
                        v-bind:class="{ selected: forEmbroidery }"
                        @click.prevent="toggleEmbroidery"
                    >
                        Embroidery
                    </button>
                    <!-- MORE CRAFTS GO HERE -->
                </div>
            </div>
            <div class="form-element">
                <div />
                <div class="option-buttons">
                    <button id="submit" type="submit">Create Tool</button>
                    <p id="cancel" @click="cancel">Cancel Create</p>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "ToolCreate",
    mounted() {},
    data() {
        return {
            validationErrors: [],
            title: "",
            description: "",
            acquired: null,
            status: "",
            forSpinning: false,
            forWeaving: false,
            forKnitting: false,
            forCrocheting: false,
            forSewing: false,
            forEmbroidery: false,
            image: null,
            imageURL: "",
            imageStatus: "Upload",
        };
    },
    methods: {
        toggleSpinning: function () {
            this.forSpinning = !this.forSpinning;
        },
        toggleWeaving: function () {
            this.forWeaving = !this.forWeaving;
        },
        toggleKnitting: function () {
            this.forKnitting = !this.forKnitting;
        },
        toggleCrocheting: function () {
            this.forCrocheting = !this.forCrocheting;
        },
        toggleSewing: function () {
            this.forSewing = !this.forSewing;
        },
        toggleEmbroidery: function () {
            this.forEmbroidery = !this.forEmbroidery;
        },
        async submit() {
            this.validationErrors = [];
            const errorsArr = [];
            if (this.title.length == 0)
                errorsArr.push("Title cannot be empty.");
            if (this.title.length > 100)
                errorsArr.push("Title cannot be longer than 100 characters.");

            if (errorsArr.length > 0) {
                this.validationErrors = errorsArr;
            } else {
                const tool = {
                    user_id: this.$store.state.sessionUser.id,
                    title: this.title,
                    description: this.description,
                    acquired: this.acquired,
                    status: this.status,
                    for_spinning: this.forSpinning,
                    for_weaving: this.forWeaving,
                    for_knitting: this.forKnitting,
                    for_crocheting: this.forCrocheting,
                    for_sewing: this.forSewing,
                    for_embroidery: this.forEmbroidery,
                    image_url: this.imageURL,
                };
                console.log(tool)
                const response = await fetch("/api/tools/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(tool),
                });
                if (response.ok) {
                    const data = await response.json();
                    this.$router.push(`/tools/${data.id}`);
                }
            }
        },
        cancel() {
            this.$router.back();
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
    },
    mutations: {
        ...mapMutations,
    },
};
</script>

<style scoped>
.tool-form-body {
    margin-left: 25%;
    margin-right: 25%;
    margin-top: 48px;
    margin-bottom: 48px;
}

.tool-form {
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

select {
    font-size: 14px;
    font-family: "Open Sans", sans-serif;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
    padding-top: 6px;
    padding-bottom: 6px;
    padding-left: 10px;
    padding-right: 10px;
}

.crafts-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, 150px);
    justify-content: space-between;

    row-gap: 6px;
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

#submit {
    width: 100%;
    font-size: 16px;
    margin-top: 6px;
    font-weight: normal;
    letter-spacing: 2px;
    color: white;
    background-color: var(--color-primary-contrast);
    margin-bottom: 48px;
}

.error-container {
    display: flex;
    flex-direction: column;
    margin: 0px;
    text-align: center;
}

.error {
    color: var(--color-primary-contrast);
    font-size: 16px;
    font-weight: bold;
    text-align: center;
}

.option-buttons {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 4px;
}

#cancel {
    width: 100%;
    font-size: 16px;
    margin-top: 6px;
    font-weight: normal;
    letter-spacing: 1.5px;
    color: var(--color-primary-contrast);
    background-color: white;
    margin-bottom: 48px;
    font-family: "Open Sans", sans-serif;
    padding-top: 4px;
    padding-bottom: 4px;
    border-radius: 4px;
    border: 1px solid var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
}

#cancel:hover {
    cursor: pointer;
}

#cancel:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.image-input {
    width: 100%;
}

.image-input > input {
    width: 100%;
    border: none;
}

.tool-image {
    width: 100%;
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
</style>
