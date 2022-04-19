<template>
    <div class="auth-body">
        <div class="auth-form">
            <h2>Log in to an existing account</h2>
            <div v-if="$store.state.loginFormErrors">
                <p id="login-form-error">{{ $store.state.loginFormErrors }}</p>
            </div>
            <form @submit.prevent="login">
                <label for="email">Enter email address</label>
                <input
                    type="email"
                    name="email"
                    v-model="form.email"
                    required="true"
                    placeholder="Email address"
                />
                <label for="password">Enter password</label>
                <input
                    type="password"
                    name="password"
                    v-model="form.password"
                    required="true"
                    placeholder="Password"
                />
                <button type="submit">LOG IN</button>
                <p id="demo-button" @click="demoLogin">DEMO LOG IN</p>
            </form>
            <p>Don't have an account yet?</p>
            <router-link to="/signup" id="auth-link">Sign up here</router-link>
        </div>
    </div>
</template>


<script>
import { mapMutations } from "vuex";

export default {
    name: "Login",
    components: {},
    mounted() {
        this.$store.commit("clearLoginFormErrors");
    },
    data() {
        return {
            form: {
                email: "",
                password: "",
            },
            showError: false,
        };
    },
    methods: {
        async login() {
            this.$store.commit("clearLoginFormErrors");
            const email = this.form.email;
            const password = this.form.password;
            const response = await fetch("/api/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    email,
                    password,
                }),
            });
            if (response.ok) {
                const data = await response.json();
                this.$store.commit("logIn", data);
                this.$router.push("/");
                return null;
            } else {
                this.$store.commit("setLoginFormErrors");
            }
        },
        async demoLogin() {
            const email = "demo@demo.com";
            const password = "demoPassword123";
            const response = await fetch("/api/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    email,
                    password,
                }),
            });
            if (response.ok) {
                const data = await response.json();
                this.$store.commit("logIn", data);
                this.$router.push("/");
                return null;
            }
        },
        state: {
            formErrors: false,
        },
        mutations: {
            ...mapMutations,
        },
    },
};
</script>

<style scoped>
.auth-body {
    background-image: url("https://knotelry.s3.amazonaws.com/splash1.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: bottom;
    margin: 0;
    padding: 0;
    min-height: calc(100vh - 70px);
    height: 100%;
    display: grid;
    grid-template-columns: 40% 60%;
}

.auth-form {
    background-color: rgba(245, 242, 240, 0.7);
    min-height: calc(100vh - 70px);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

form {
    display: flex;
    flex-direction: column;
}

form > label {
    font-family: "Open Sans", sans-serif;
    margin-top: 4px;
}

form > input {
    width: 200px;
    margin-left: auto;
    margin-right: auto;
    font-family: "Open Sans", sans-serif;
    text-align: center;
    border-radius: 6px;
    padding: 4px;
    border: 1px solid var(--color-shadow);
    margin-top: 4px;
    margin-bottom: 4px;
}

form > button {
    width: 200px;
    margin-left: auto;
    margin-right: auto;
    font-family: "Open Sans", sans-serif;
    background-color: var(--color-shadow);
    border: 1px solid var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    border-radius: 6px;
    color: #f5f2f0;
    margin-top: 12px;
}

form > button:hover {
    cursor: pointer;
}

.auth-form > p {
    margin-top: 24px;
}

#auth-link {
    text-decoration: none;
    font-family: "Open Sans", sans-serif;
    color: var(--color-shadow);
    font-weight: bold;
    margin-top: -12px;
}

#demo-button {
    background-color: var(--color-shadow);
    width: 200px;
    margin-left: auto;
    margin-right: auto;
    padding-top: 4px;
    padding-bottom: 4px;
    border-radius: 6px;
    color: #f5f2f0;
    margin-top: 6px;
    font-size: 14px;
}

#demo-button:hover {
    cursor: pointer;
}

#login-form-error {
    font-weight: bold;
}
</style>
