import App from './App.svelte';

const app = new App({
	target: document.getElementsByTagName("main")[0],
	props: {
	}
});

window.app = app;

export default app;
