<template>
    <div class="stash-form-body">
        <form class="stash-form" @submit.prevent="submit">
            <div class="form-element">
                <div />
                <h2>Creating New Stash Item</h2>
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
            <!-- STASH ITEM METADATA -->
            <div class="form-element">
                <label for="title">Title:</label>
                <input
                    type="text"
                    placeholder="Enter a title for your stash item"
                    v-model="title"
                />
            </div>
            <div class="form-element">
                <div />
                <div class="option-buttons">
                    <button id="submit" type="submit">Stash It!</button>
                    <p id="cancel" @click="cancel">Cancel Create</p>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "StashCreate",
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
            if (!this.title || this.title?.length == 0)
                errorsArr.push("Title cannot be empty.");
            if (this.title?.length > 100)
                errorsArr.push("Title cannot be longer than 100 characters.");

            if (errorsArr.length > 0) {
                this.validationErrors = errorsArr;
                window.scrollTo(0, 0);
            } else {
                const stashItem = {
                    user_id: this.$store.state.sessionUser.id,
                    title: this.title,
                    description: null,
                    type: null,

                    status: null,
                    tags: null,
                    attributes: null,
                    stored_in: null,

                    acquired: null,
                    acquired_from: null,
                    acquired_price: null,
                    acquired_currency: null,

                    colors: null,

                    dyer_name: null,
                    colorway_name: null,

                    fiber_content: null,
                    fiber_quantity: null,
                    fiber_quantity_unit: null,

                    yarn_weight: null,
                    length_per_skein: null,
                    length_unit: null,
                    weight_per_skein: null,
                    weight_unit: null,
                    skeins_stashed: null,
                    length_stashed: null,
                    weight_stashed: null,
                    is_handspun: null,

                    fabric_width: null,
                    fabric_width_unit: null,
                    fabric_weight: null,
                    fabric_weight_unit: null,
                    fabric_weight_area_unit: null,
                    fabric_pattern_repeat_width: null,
                    fabric_pattern_repeat_height: null,
                    fabric_pattern_repeat_unit: null,

                    length_per_bobbin: null,
                    bobbins_stashed: null,
                    plies: null,

                    notes: null,
                };
                const response = await fetch("/api/stash/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(stashItem),
                });
                if (response.ok) {
                    const data = await response.json();
                    this.$router.push(`/stash/${data.id}/edit`);
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
.stash-form-body {
    margin-left: 25%;
    margin-right: 25%;
    margin-top: 48px;
    margin-bottom: 48px;
}

.stash-form {
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
