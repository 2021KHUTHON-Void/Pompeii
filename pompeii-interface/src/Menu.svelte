<script>
	import Menuitems from './Menuitems.svelte'

    // 메뉴 바 항목들
    const navItems = [
        { label: "하이 폼페이!", href: "#article1" },
        { label: "퀴즈", href: "#article2" },
        { label: "재난 뉴스", href: "#article3" },
        { label: "기술", href: "#article4" } 
    ];
</script>

<style>
	nav {
		background-color: #444444;
		font-family: 맑은고딕, Malgun Gothic, dotum, gulim, sans-serif;
		height: 70px;
		top: 0;	
	}

	.inner {
		max-width: 500px;
		padding-left: 10px;
		padding-right: 10px;
		margin: auto;
		box-sizing: border-box;
		display: flex;
		align-items: center;
		height: 100%;
	}

	.logo img{
		display: flex;
		position: absolute;
		width: 100px;
		left: 20px;
		top: 15px
	}

	.navbar-list {
		display: flex;
		padding: 0;	
		width: 100%;
		justify-content: space-between;
		margin: 0;
	}
</style>

<nav>
	<div class="logo"><img src="./static/logo.png" alt=":("></div>
	<div class="inner">
        <ul class='navbar-list'>
        {#each navItems as item}
            <Menuitems {item}/>
        {/each}
        </ul>
    </div>
</nav>