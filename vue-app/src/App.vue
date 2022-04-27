<template>
    <div id="app">
        <nav>
            <div class="nav-section">
                <router-link to="/" id="home-link">knotelry</router-link>
                <!-- <router-link to="/patterns">patterns</router-link>
                <router-link to="/yarns">yarns</router-link>
                <router-link to="/community">community</router-link>
                <router-link to="/search">advanced search</router-link> -->
            </div>
            <div v-if="$store.state.authenticated" class="nav-section">
                <p @mouseover="hover = true">
                    Welcome, {{ $store.state.sessionUser.username }}!
                </p>
                <div
                    id="dropdown-content"
                    v-if="hover"
                    @mouseover="hover = true"
                    @mouseleave="hover = false"
                >
                    <router-link :to="`/users/${$store.state.sessionUser.id}`"
                        >User Profile
                    </router-link>
                    <router-link
                        :to="`/users/${$store.state.sessionUser.id}/projects`"
                    >
                        My Projects</router-link
                    >
                    <router-link
                        :to="`/users/${$store.state.sessionUser.id}/stash`"
                    >
                        My Stash
                    </router-link>
                    <router-link
                        :to="`/users/${$store.state.sessionUser.id}/toolbox`"
                    >
                        My Toolbox
                    </router-link>
                </div>
                <p>|</p>
                <p @click="logout" id="signout-button">Sign Out</p>
            </div>
            <div v-else class="nav-section">
                <router-link to="/login">Login</router-link> |
                <router-link to="/signup">Sign Up</router-link>
            </div>
        </nav>
        <router-view />
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    data() {
        return {
            hover: false,
        };
    },
    methods: {
        async logout() {
            const response = await fetch("/api/auth/logout");
            if (response.ok) {
                this.$store.commit("logOut");
                this.$router.push("/");
                return null;
            }
        },
    },
    mutations: {
        ...mapMutations,
    },
};
</script>

<style>
body {
    background-color: var(--color-background);
    margin: 0;
    min-width: 1000px;
}

#app {
    font-family: "Open Sans", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: var(--color-shadow);
    padding: 0;
    margin: 0;
}

nav {
    background-color: var(--color-nav);
    display: flex;
    justify-content: space-between;
    padding-top: 6px;
    padding-bottom: 8px;
    padding-left: 24px;
    padding-right: 24px;
    margin: 0;
}

nav a {
    text-decoration: none;
    align-self: center;
    color: var(--color-shadow);
    z-index: 10;
}

nav p {
    z-index: 10;
}

.nav-section {
    display: flex;
    column-gap: 20px;
    align-self: center;
}

#home-link {
    color: var(--color-primary-contrast);
    font-family: "Pacifico", serif;
    font-size: 32px;
    margin-right: 12px;
}

#signout-button:hover {
    cursor: pointer;
}

#dropdown-content {
    position: absolute;
    width: 186px;
    padding-top: 60px;
    padding-bottom: 20px;
    background-color: var(--color-nav);
    border-bottom-right-radius: 4px;
    box-shadow: 0px 4px 2px -1px var(--color-shadow);
    right: 120px;
    top: 0px;
    display: flex;
    flex-direction: column;
    row-gap: 16px;
}

#dropdown-content > a {
    font-size: 14px;
}

#dropdown-content > p {
    font-size: 14px;
}

#dropdown-content > a:hover {
    font-weight: bold;
}

#dropdown-content > p:hover {
    font-weight: bold;
}

:root {
    --color-background: #fffcf9;
    --color-nav: #f4eae6;
    --color-primary-contrast: #e57f84;
    --color-shadow: #2f5061;
}
</style>
