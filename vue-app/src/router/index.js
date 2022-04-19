import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import Login from '../views/LoginView.vue'
import Signup from '../views/SignupView.vue'

import User from '../views/UserView.vue'
import UserEdit from '../views/UserEditView.vue'

import Toolbox from '../views/Tools/ToolboxView.vue'
import ToolDetail from '../views/Tools/ToolDetailView.vue'
import ToolCreate from '../views/Tools/ToolCreateView.vue'
import ToolEdit from '../views/Tools/ToolEditView.vue'
import ToolDelete from '../views/Tools/ToolDeleteView.vue'

import Stash from '../views/Stash/StashView.vue'
import StashDetail from '../views/Stash/StashDetailView.vue'
import StashCreate from '../views/Stash/StashCreateView.vue'
import StashEdit from '../views/Stash/StashEditView.vue'
import StashDelete from '../views/Stash/StashDeleteView.vue'

import Projects from '../views/Projects/ProjectsView.vue'
import ProjectDetail from '../views/Projects/ProjectDetailView.vue'
import ProjectCreate from '../views/Projects/ProjectCreateView.vue'
import ProjectEdit from '../views/Projects/ProjectEditView.vue'
import ProjectDelete from '../views/Projects/ProjectDeleteView.vue'

import PNF from '../views/PNFView.vue'

const routes = [
	{
		path: '/',
		name: 'home',
		component: HomeView
	},
	{
		path: '/login',
		name: 'login',
		component: Login
	},
	{
		path: '/signup',
		name: 'signup',
		component: Signup
	},
	{
		path: '/users/:id',
		name: 'user',
		component: User
	},
	{
		path: '/users/edit',
		name: 'userEdit',
		component: UserEdit
	},
	{
		path: '/users/:id/toolbox',
		name: 'usersTools',
		component: Toolbox
	},
	// -------------------- TOOLS -------------------- //
	{
		path: '/tools/create',
		name: 'toolCreate',
		component: ToolCreate
	},
	{
		path: '/tools/:toolId/edit',
		name: 'toolEdit',
		component: ToolEdit
	},
	{
		path: '/tools/:toolId/delete',
		name: 'toolDelete',
		component: ToolDelete
	},
	{
		path: '/tools/:toolId',
		name: 'toolDetail',
		component: ToolDetail
	},
	// -------------------- STASH -------------------- //
	{
		path: '/users/:id/stash',
		name: 'usersStash',
		component: Stash
	},
	{
		path: '/stash/:stashId',
		name: 'stashDetail',
		component: StashDetail
	},
	{
		path: '/stash/create',
		name: 'stashCreate',
		component: StashCreate
	},
	{
		path: '/stash/:stashId/edit',
		name: 'stashEdit',
		component: StashEdit
	},
	{
		path: '/stash/:stashId/delete',
		name: 'stashDelete',
		component: StashDelete
	},
	// -------------------- PROJECTS -------------------- //
	{
		path: '/users/:id/projects',
		name: 'usersProjects',
		component: Projects
	},
	{
		path: '/projects/:projectId',
		name: 'projectDetail',
		component: ProjectDetail
	},
	{
		path: '/projects/create',
		name: 'projectCreate',
		component: ProjectCreate
	},
	{
		path:'/projects/:projectId/edit',
		name: 'projectEdit',
		component: ProjectEdit
	},
	{
		path: '/projects/:projectId/delete',
		name: 'projectDelete',
		component: ProjectDelete
	},
	{
		path: '/404',
		name: '404',
		component: PNF
	},

	// {
	//   path: '/about',
	//   name: 'about',
	//   // route level code-splitting
	//   // this generates a separate chunk (about.[hash].js) for this route
	//   // which is lazy-loaded when the route is visited.
	//   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
	// }
]

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
})

export default router
