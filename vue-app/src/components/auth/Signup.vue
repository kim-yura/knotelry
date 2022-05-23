<template>
    <div class="auth-body">
        <div class="auth-form">
            <h2>Sign up for a new account</h2>
            <ul v-if="$store.state.signupFormErrors.length">
                <li
                    v-for="error in $store.state.signupFormErrors"
                    :key="error.message"
                >
                    {{ error.message }}
                </li>
            </ul>
            <form @submit.prevent="signup">
                <label for="email">Enter email address</label>
                <input
                    type="email"
                    name="email"
                    v-model="form.email"
                    required="true"
                    placeholder="Email address"
                />
                <label for="username">Enter username</label>
                <input
                    type="text"
                    name="username"
                    v-model="form.username"
                    required="true"
                    placeholder="Username"
                />
                <label for="password">Enter a password</label>
                <input
                    type="password"
                    name="password"
                    v-model="form.password"
                    required="true"
                    placeholder="Password"
                />
                <label for="password">Enter password again</label>
                <input
                    type="password"
                    name="passwordRepeat"
                    v-model="form.passwordRepeat"
                    required="true"
                    placeholder="Password"
                />
                <button type="submit">SIGN UP</button>
            </form>
            <p>Already have an account?</p>
            <router-link to="/login" id="auth-link">Log in here</router-link>
        </div>
    </div>
</template>


<script>
import { mapMutations } from "vuex";

export default {
    name: "Signup",
    components: {},
    mounted() {
        this.$store.commit("clearSignupFormErrors");
    },
    data() {
        return {
            form: {
                email: "",
                username: "",
                password: "",
            },
            showError: false,
        };
    },
    methods: {
        async signup() {
            this.$store.commit("clearSignupFormErrors");
            const email = this.form.email;
            const username = this.form.username;
            const password = this.form.password;
            const passwordRepeat = this.form.passwordRepeat;

            if (password !== passwordRepeat) {
                this.$store.commit(
                    "setSignupFormErrors",
                    "Passwords must match!"
                );
            }

            if (this.$store.state.signupFormErrors.length === 0) {
                const response = await fetch("/api/auth/signup", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        email,
                        username,
                        password,
                    }),
                });
                if (response.ok) {
                    const data = await response.json();
                    this.$store.commit("signUp", data);
                    this.$router.push("/");
                    return null;
                } else {
                    const data = await response.json();
                    const errorsArr = Object.values(data)[0];
                    errorsArr.forEach((error) => {
                        const arr = error.split(" : ");
                        this.$store.commit("setSignupFormErrors", arr[1]);
                    });
                }
            }
        },
        mutations: {
            ...mapMutations,
        },
    },
};
</script>

<style scoped>
.auth-body {
    background-image: url("https://knotelry.s3.amazonaws.com/splash2.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    margin: 0;
    padding: 0;
    min-height: calc(100vh - 68px) ;
    height: 100%;
    display: grid;
    grid-template-columns: 40% 60%;
}

.auth-form {
    background-color: rgba(245, 242, 240, 0.85);
    min-height: calc(100vh - 68px) ;
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

ul {
    padding-left: 0px;
}

li {
    list-style: none;
    font-weight: bold;
}
</style>
