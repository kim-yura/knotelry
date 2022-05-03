<template>
    <div class="project-form-body">
        <form class="project-form" @submit.prevent="submit">
            <div class="form-element">
                <div />
                <h2>Creating New Project</h2>
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
                <label for="title">Project Title:</label>
                <input
                    type="text"
                    placeholder="Enter a title for your project"
                    v-model="title"
                />
            </div>
            <div class="form-element">
                <div />
                <div class="option-buttons">
                    <button id="submit" type="submit">Create Project!</button>
                    <p id="cancel" @click="cancel">Cancel Create</p>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "ProjectCreate",
    data() {
        return {
            validationErrors: [],
            title: null,
        };
    },
    methods: {
        async submit() {
            this.validationErrors = [];
            const errorsArr = [];
            if (!this.title || this.title?.length == 0) errorsArr.push("Title cannot be empty.");
            if (this.title?.length > 100) errorsArr.push("Title cannot be longer than 100 characters.");

            if (errorsArr.length > 0) {
                this.validationErrors = errorsArr;
                window.scrollTo(0, 0);
            } else {
                const project = {
                    user_id: this.$store.state.sessionUser.id,
                    title: this.title,
                    description: null,
                    craft_types: null,
                    pattern_name: null,
                    pattern_author: null,
                    link_to_pattern: null,
                    size_made: null,

                    tags: null,
                    status: null,
                    attributes: null,
                    stored_in: null,

                    start_date: null,
                    end_date: null,

                    yarn_weight: null,
                    grist: null,
                    grist_unit: null,
                    wpi: null,
                    plies_count: null,

                    twist_direction_singles: null,
                    twist_direction_plied: null,
                    twist_angle: null,
                    drive_ratio_singles: null,
                    drive_ratio_plied: null,
                    finished_weight: null,
                    weight_unit: null,

                    warp_yarn: null,
                    weft_yarn: null,
                    epi: null,
                    total_ends: null,
                    ppi: null,
                    draft_notes: null,
                    width_in_reed: null,
                    length: null,
                    length_unit: null,
                    finished_length: null,

                    needle_sizes: null,
                    gauge_count: null,
                    gauge_unit: null,
                    gauge_rows: null,
                    gauge_size_width: null,
                    gauge_size_height: null,
                    gauge_size_unit: null,

                    notes: null,
                };
                const response = await fetch("/api/projects/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(project),
                });
                if (response.ok) {
                    const data = await response.json();
                    this.$router.push(`/projects/${data.id}/edit`);
                }
            }
        },
        cancel() {
            this.$router.back();
        },
    },
    mutations: {
        ...mapMutations,
    },
};
</script>

<style scoped>
.project-form-body {
    margin-left: 25%;
    margin-right: 25%;
    margin-top: 48px;
    margin-bottom: 48px;
}

.project-form {
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
</style>
