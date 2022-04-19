<template>
    <div class="stash-delete-body">
        <form class="stash-form" @submit.prevent="submit">
            <h2>Deleting Stash Item</h2>
            <h4>{{ this.$store.state.selectedStashItem?.title }}</h4>
            <img
                v-if="this.$store.state.selectedStashItem?.stashItemImages.length"
                :src="this.$store.state.selectedStashItem?.stashItemImages[0].imageURL"
                alt="Stash item image"
                class="stash-image"
            />

            <img
                v-else
                src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                alt="No image found"
                class="stash-image"
            />
            <p>Are you sure you want to delete this stash item?</p>
            <div class="option-buttons">
                <button id="submit" type="submit">Delete Item</button>
                <p id="cancel" @click="cancel">Cancel Delete</p>
            </div>
        </form>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "StashDelete",
    mounted() {
        const data = loadStash(this.$route.params.stashId).then((data) => {
            if (data && data?.userId == this.$store.state.sessionUser?.id) {
                this.$store.commit("setSelectedStashItem", data);
            } else {
                this.$router.push("/404");
            }
        });
    },
    methods: {
        async submit() {
            const stashItem = {
                id: this.$route.params.stashId,
            };
            const response = await fetch("/api/stash/", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(stashItem),
            });
            if (response.ok) {
                const data = await response.json();
                this.$router.push(
                    `/users/${this.$store.state.sessionUser.id}/stash`
                );
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

const loadStash = async (id) => {
    const response = await fetch(`/api/stash/${id}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return false;
    }
};
</script>

<style scoped>
.stash-delete-body {
    display: flex;
    flex-direction: column;
    margin-left: 35%;
    margin-right: 35%;
    margin-top: 48px;
    margin-bottom: 48px;
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
    letter-spacing: 2px;
    color: var(--color-primary-contrast);
    background-color: white;
    margin-bottom: 48px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
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

.stash-image {
    width: 100%;
    height: auto;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
}
</style>
