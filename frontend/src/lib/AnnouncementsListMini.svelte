<script>
  import Post from "$lib/Post.svelte";
  import Loading from "$lib/Loading.svelte";
  import PostPopup from "$lib/PostPopup.svelte";
  import { formatDateTime } from "./formatDateTime";

  export let max;
  export let posts;
  export let admin = false;
  export let href = '';

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

  function navigate() {
    window.location.href = href;
  }

  $: allPosts = [...allPosts, ...newPosts]

  let postData = null;
  let postDelete = null;
</script>

<div class="flex flex-col items-center max-h-screen space-y-7 mx-20">
  {#each allPosts as p, i}
    {#if i > 0}
      <hr class="h-[0.5px] bg-gray-200 border-0 max-w-200">
    {/if}

    <Post 
      id={p.id}
      subject={p.subject}
      author={p.author}
      body={p.body} 
      time={formatDateTime(p.datetimePosted).time} 
      date={formatDateTime(p.datetimePosted).date}
      admin={admin}
      tags={p.tags}
      on:openPost={(e) => postData = e.detail}
      on:deletePost={(e) => postDelete = e.detail}
    />
  {/each}

  {#if isLoading}
    <Loading />
  {:else}
    {#if offset < max}
      {#if href}
        <button
          class="max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 py-2 px-4 rounded inter-body text-[13px]"
          on:click={navigate}
          disabled={isLoading}
        >
          Load more →
        </button>
        <p class="text-white text-[5px]">...</p>
      {:else}
        <button
          class="max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 pt-2 px-4 rounded inter-body text-[13px]"
          on:click={updatePosts}
          disabled={isLoading}
        >
          Load more ↓
        </button>
      {/if}
      <br>
    {/if}
  {/if}
</div>

{#if postData}
  <PostPopup 
    posts={allPosts}
    id={postData.id}
    author={postData.author}
    title={postData.subject}
    ogTitle={postData.subject}
    body={postData.body}
    ogBody={postData.body}
    selectedTags={postData.tags}
    text="X"
  />
{/if}


