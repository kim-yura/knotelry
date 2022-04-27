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
		// ---------- TOOLS ---------- //
		usersTools: [],
		spinningTools: [],
		weavingTools: [],
		knittingTools: [],
		crochetingTools: [],
		sewingTools: [],
		embroideryTools: [],
		selectedTool: null,
		// ---------- STASH ---------- //
		usersStash: [],
		selectedStashItem: null,
		// ---------- PROJECTS ---------- //
		usersProjects: [],
		spinningProjects: [],
		knittingProjects: [],
		crochetingProjects: [],
		sewingProjects: [],
		selectedProject: null,
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
		// ---------- TOOLS ---------- //
		setUsersTools(state, toolsData) {
			if (Array.isArray(toolsData)) {
				state.usersTools = toolsData;
			} else {
				state.usersTools = Object.values(toolsData)[0];
			};
		},
		setUsersToolCategories(state, toolsData) {
			const spinningArr = [];
			const weavingArr = [];
			const knittingArr = [];
			const crochetingArr = [];
			const sewingArr = [];
			const embroideryArr = [];
			Object.values(toolsData)[0].forEach(tool => {
				if (tool.forSpinning) {
					spinningArr.push(tool);
				};
				if (tool.forWeaving) {
					weavingArr.push(tool);
				};
				if (tool.forKnitting) {
					knittingArr.push(tool);
				};
				if (tool.forCrocheting) {
					crochetingArr.push(tool);
				};
				if (tool.forSewing) {
					sewingArr.push(tool);
				};
				if (tool.forEmbroidery) {
					embroideryArr.push(tool);
				};
			});
			state.spinningTools = spinningArr;
			state.weavingTools = weavingArr;
			state.knittingTools = knittingArr;
			state.crochetingTools = crochetingArr;
			state.sewingTools = sewingArr;
			state.embroideryTools = embroideryArr;
		},
		setSelectedTool(state, tool) {
			state.selectedTool = tool;
		},
		// ---------- STASH ---------- //
		setUsersStash(state, stashData) {
			if (Array.isArray(stashData)) {
				state.usersStash = stashData;
			} else {
				state.usersStash = Object.values(stashData)[0];
			};
		},
		setSelectedStashItem(state, stashItem) {
			state.selectedStashItem = stashItem;
		},
		// ---------- PROJECTS ---------- //
		setUsersProjects(state, projectsData) {
			if (Array.isArray(projectsData)) {
				state.usersProjects = projectsData;
			} else {
				state.usersProjects = Object.values(projectsData)[0];
			};
		},
		setUsersProjectCategories(state, projectsData) {
			const spinningArr = [];
			const knittingArr = [];
			const sewingArr = [];
			Object.values(projectsData)[0].forEach(project => {
				if (project.craftTypes.includes('spinning')) {
					spinningArr.push(project);
				};
				if (project.craftTypes.includes('knitting')) {
					knittingArr.push(project);
				};
				if (project.craftTypes.includes('sewing')) {
					sewingArr.push(project);
				};
			});
			state.spinningProjects = spinningArr;
			state.knittingProjects = knittingArr;
			state.sewingProjects = sewingArr;
		},
		setSelectedProject(state, project) {
			state.selectedProject = project;
		},
	},
	actions: {
	},
	plugins: [createPersistedState()],
})
