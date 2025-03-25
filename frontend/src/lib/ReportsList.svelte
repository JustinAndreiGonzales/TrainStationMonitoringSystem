<script>
  import Post from "$lib/Post.svelte";
  import Loading from "$lib/Loading.svelte"
  import { formatDateTime } from "./formatDateTime";

  export let current = 5;
  export let posts;

  $: current = current;
    
</script>

<div class="flex flex-col items-center min-h-screen space-y-7 pb-25">
  {#each posts as p, i}
    {#if i > -1}
      {#if i > 0}
        <hr class="w-210 h-[0.5px] bg-gray-200 border-0">
      {/if}

      <Post 
        tags={p.station.split(',')}
        subject={p.subject}
        body={p.body} 
        time={formatDateTime(p.datetimeReported).time} 
        date={formatDateTime(p.datetimeReported).date}
      />
    {/if}
  {/each}
</div>
