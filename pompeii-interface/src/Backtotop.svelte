<script>
    import { fly } from 'svelte/transition'
    import { onMount, onDestroy } from 'svelte';
    let show = false;

    function scrollUp() {
        document.body.scrollIntoView({behavior: "smooth"})
    }

    onMount(() => {
        window.onscroll = () => {
            if (window.scrollY > 60) {
                show = true
            } else {
                show = false
            }
        }
    });

    onDestroy(() => {
        window.onscroll = () => {}
    });
</script>

<style>
    #backtotop {
        background-color: rgb(250, 200, 125);
        color: #fff;
        border-radius: 20px;
        border: none;
        width: 50px;
        height: 50px;
        position: fixed;
        right: 4%;
        bottom: 10%;
        box-shadow: 0 3px 6px rgb(0 0 0 / 15%);
    }

</style>

{#if (show)}
    <button id="backtotop"
    transition:fly="{{ y : 200, duration:400}}"
    on:click={scrollUp}>
        ▲
    </button>
{/if}