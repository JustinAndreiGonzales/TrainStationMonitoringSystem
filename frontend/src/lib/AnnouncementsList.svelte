<script>
  import Post from "$lib/Post.svelte";
  import Loading from "$lib/Loading.svelte"
  import { formatDateTime } from "./formatDateTime";

  export let max;
  export let posts;
  let offset = posts.length;
  let allPosts = [...posts];
  let newPosts = [];
  let isLoading = false;

  async function updatePosts() {
    isLoading = true;
    
    try {
      const res = await fetch(`https://trenph.up.railway.app/api/announcements/?format=json&offset=${offset}&limit=5`);
      if (!res.ok) throw new Error("Failed to load more posts");

      const fetchedPosts = await res.json();
      newPosts = fetchedPosts.results;
      offset += 5; 
    } catch (error) {
      console.error("Error fetching posts:", error);
      offset -= 5; 
    } finally {
      isLoading = false;
    }
  }

  $: allPosts = [...allPosts, ...newPosts]
</script>

<div class="flex flex-col items-center min-h-screen space-y-7 pb-25">
  {#each allPosts as p, i}
    {#if i > 0}
      <hr class="w-210 h-[0.5px] bg-gray-200 border-0">
    {/if}

    <Post 
      title='[{p.author}] {p.subject}' 
      body={p.body} 
      time={formatDateTime(p.datetimePosted).time} 
      date={formatDateTime(p.datetimePosted).date}
    />
  {/each}

  {#if isLoading}
    <Loading />
  {:else}
    {#if offset < max}
    <button
      class="max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 py-2 px-4 rounded inter-body text-[13px]"
      on:click={updatePosts}
      disabled={isLoading}
    >
      Load more ↓
    </button>
    {/if}
  {/if}
</div>
