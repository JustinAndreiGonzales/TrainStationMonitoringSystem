<script>
  import Foo from '$lib/dummy/Foo.svelte';
  import Bar from '$lib/dummy/Bar.svelte';

  let items = ['Apple', 'Banana', 'Cherry'];
  let barText = null; 
</script>

<div class="space-y-2">
  {#each items as item}
    <Foo text={item} on:openBar={(e) => barText = e.detail.text} />
  {/each}
</div>

{#if barText}
  <Bar text={barText} />
{/if}
