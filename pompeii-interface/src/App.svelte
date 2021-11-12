<script>
    import Menu from './Menu.svelte'
    import Backtotop from './Backtotop.svelte'
	import Chat from './Chat.svelte'
	import Article from './Articles.svelte'
</script>

<style>
	div {
		text-align: left;
		box-sizing: border-box;
		display: block;
	}

	:global(body) {
		padding: 0;
		margin: 0;
	}

	:global(html) {
		scroll-behavior: smooth;
	}

</style>

<div>
	<Menu/>
	<Chat/>
	<Backtotop/>
	<Article/>
</div>