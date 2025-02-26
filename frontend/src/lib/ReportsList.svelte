<script>
  import Post from "$lib/Post.svelte";
  import Loading from "$lib/Loading.svelte"
  import { formatDateTime } from "./formatDateTime";

  let current = 5;
  export let posts;

  $: current = current;
    
</script>

<div class="flex flex-col items-center min-h-screen space-y-7 pb-25">
  {#each posts as p, i}
    {#if i < current}
      {#if i > 0}
        <hr class="w-210 h-[0.5px] bg-gray-200 border-0">
      {/if}

      <Post 
        title='[{p.station}] {p.subject}' 
        body={p.body} 
        time={formatDateTime(p.datetimeReported).time} 
        date={formatDateTime(p.datetimeReported).date}
      />
    {/if}
  {/each}

  {#if current < posts.length}
  <button
    class="max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 py-2 px-4 rounded inter-body text-[13px]"
  >
    Load more ↓
  </button>
  {/if}
</div>
