<style>
	li {
		list-style-type: none;
		position: relative;
	}

	li:before {
		content: "";
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		height: 1px;
	}

	a {
		color: #bbbbbb;
		text-decoration: none;
		font-weight: bold;
		display: inline-flex;
		height: 45px;
		align-items: center;
		padding: 0 10px;
		font-size: 20px;
	}

	@media only screen and (max-width: 767px) {
		a {
			display: none;
		}
	}

    .onmouse {
		color: rgb(250, 200, 125);
    }
</style>

<script>
    export let item;
    let onmouse;

    function enter() {
        onmouse = true;
    } 

    function leave() {
        onmouse = false;
    }
</script>

<li on:mouseenter={enter} on:mouseleave={leave} >
    <a href={item.href} class:onmouse>{item.label}</a>
</li>