import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';

export default createStore({
	state: {
		// ---------- AUTHENTICATION ---------- //
		authenticated: false,
		sessionUser: null,
		loginFormErrors: false,
		signupFormErrors: [],
		// ---------- USER PROFILE ---------- //
		selectedUser: null,
		usersPhotos: [],
	},
	getters: {
	},
	mutations: {
		// ---------- AUTHENTICATION ---------- //
		logIn(state, user) {
			state.authenticated = true,
				state.sessionUser = user
		},
		logOut(state) {
			state.authenticated = false;
			state.sessionUser = null;
		},
		signUp(state, user) {
			state.authenticated = true;
			state.sessionUser = user;
		},
		setLoginFormErrors(state) {
			state.loginFormErrors = "There was an error with your login/password."
		},
		clearLoginFormErrors(state) {
			state.loginFormErrors = false;
		},
		setSignupFormErrors(state, error) {
			state.signupFormErrors = [...state.signupFormErrors, { "message": error }];
		},
		clearSignupFormErrors(state) {
			state.signupFormErrors = [];
		},
		// ---------- USER PROFILE ---------- //
		setSelectedUser(state, user) {
			state.selectedUser = user
		},
		clearSelectedUser(state) {
			state.selectedUser = null
		},
		setUsersPhotos(state, usersPhotos) {
			if (Array.isArray(usersPhotos)) {
				state.usersPhotos = usersPhotos;
			} else {
				state.usersPhotos = Object.values(usersPhotos)[0]
			};
		},
	},
	actions: {
	},
	plugins: [createPersistedState()],
})
