<template>
    <div class="project-delete-body">
        <form class="project-form" @submit.prevent="submit">
            <h2>Deleting Project</h2>
            <h4>{{ this.$store.state.selectedProject?.title }}</h4>
            <img
                v-if="this.$store.state.selectedProject?.imageURL"
                :src="this.$store.state.selectedProject?.imageURL"
                alt="Project image"
                class="project-image"
            />
            <p>Are you sure you want to delete this project?</p>
            <div class="option-buttons">
                <button id="submit" type="submit">Delete Project</button>
                <p id="cancel" @click="cancel">Cancel Delete</p>
            </div>
        </form>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "ProjectDelete",
    mounted() {
        const data = loadProject(this.$route.params.projectId).then((data) => {
            if (data && data?.userId == this.$store.state.sessionUser?.id) {
                this.$store.commit("setSelectedProject", data);
            } else {
                this.$router.push("/404");
            }
        });
    },
    methods: {
        async submit() {
            const project = {
                id: this.$route.params.projectId,
            };
            const response = await fetch("/api/projects/", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(project),
            });
            if (response.ok) {
                const data = await response.json();
                this.$router.push(
                    `/users/${this.$store.state.sessionUser.id}/projects`
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

const loadProject = async (projectId) => {
    const response = await fetch(`/api/projects/${projectId}`);
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
.project-delete-body {
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

.project-image {
    width: 100%;
    height: auto;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
}
</style>
