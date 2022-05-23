<template>
    <div class="groups-page">
        <div class="groups-page-left">
            <h3 v-if="usersGroups?.length == 1">
                You are in {{ usersGroups?.length }} group
            </h3>
            <h3 v-else>You are in {{ usersGroups?.length }} groups</h3>
        </div>
    </div>
</template>

<script>
export default {
    name: "Groups",
    mounted() {
        if (!this.$store.state.sessionUser?.id) {
            this.$router.push("/login");
        }
        const data = loadUser(this.$store.state.sessionUser?.id).then(
            (data) => {
                if (data) {
                    this.user = data;
                } else {
                    this.$router.push("/login");
                }
            }
        );
        const usersGroupsData = loadUsersGroups(
            this.$store.state.sessionUser?.id
        ).then((usersGroupsData) => {
            if (usersGroupsData) {
                if (Array.isArray(usersGroupsData)) {
                    this.usersGroups = usersGroupsData;
                } else {
                    this.usersGroups = Object.values(usersGroupsData)[0];
                }
            }
        });
    },
    data() {
        return {
            user: null,
            usersGroups: null,
        };
    },
    methods: {},
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

const loadUsersGroups = async (userId) => {
    const response = await fetch(`/api/groups/users/${userId}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        return false;
    }
};
</script>

<style scoped>
.groups-page {
    display: grid;
    grid-template-columns: 1fr 3fr;
    column-gap: 4%;
    border: 1px solid yellow;
}

.groups-page-left {
    min-height: calc(100vh - 68px);
    border: 1px solid yellow;
}
</style>
