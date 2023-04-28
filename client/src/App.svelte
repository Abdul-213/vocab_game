<script>
	export let name;

    let word = asd;

    function getWord() {
        fetch("./start")
          .then(d => d.text())
          .then(d => (word = d));
     }

</script>


<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
    <h1> Your word is {word}! </h1>
	<button on:click={getWord}>Get a random word</button>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>