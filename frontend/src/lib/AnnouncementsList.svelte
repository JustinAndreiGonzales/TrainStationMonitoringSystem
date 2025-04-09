<script>
  import Post from "$lib/Post.svelte";
  import Loading from "$lib/Loading.svelte";
  import Popup from "$lib/Popup.svelte";
  import PostPopup from "$lib/PostPopup.svelte";
  import { formatDateTime } from "./formatDateTime";

  export let max;
  export let posts;
  export let admin = 3;
  export let href = '';
  export let filters = [];

  let offset = posts.length;
  let allPosts = [...posts];
  let newPosts = [];
  let isLoading = false;
  let err = '';

  async function updatePosts() {
    isLoading = true;
    
    try {
      const res = await fetch(`https://trenph.up.railway.app/api/announcements/?format=json&offset=${offset}&limit=5`);
      if (!res.ok) throw new Error("Error! Failed to load more posts");

      const fetchedPosts = await res.json();
      newPosts = fetchedPosts.results;
      offset += 5; 
    } catch (error) {
      offset -= 5; 
    } finally {
      isLoading = false;
    }
  }

  async function editPost(event) {
    //const res = await fetch(`https://httpstat.us/500`);
    const res = await fetch(`https://trenph.up.railway.app/api/announcements/?format=json`);

    if(!res.ok) {
      err = 'Error! Cannot access announcement';
    }
    else {
      postData = event.detail;
    }
  }

  function navigate() {
    window.location.href = href;
  }

  $: allPosts = [...allPosts, ...newPosts]
  $: filteredPosts = filters.length ? allPosts.filter(post => post.tags.some(tag => filters.includes(tag))) : allPosts

  let postData = null;
  let postDelete = null;
</script>

<div class="flex flex-col items-center space-y-7 pb-25 sm:mx-20">
  {#each filteredPosts as p, i}
      {#if i > 0}
        <hr class="w-full h-[0.5px] bg-gray-200 border-0 max-w-200">
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
        on:openPost={(e) => editPost(e)}
        on:deletePost={(e) => postDelete = e.detail}
      />
  {/each}

  {#if !filteredPosts.length && !isLoading}
    <p class="inter-body text-sm">No available posts with selected filters.{offset < max ? " Try loading more to view them." : ""}</p>
  {/if}

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
          Load more ↓
        </button>
      {:else}
        <button
          class="max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 py-2 px-4 rounded inter-body text-[13px]"
          on:click={updatePosts}
          disabled={isLoading}
        >
          Load more ↓
        </button>
      {/if}
    {/if}
  {/if}
</div>


{#if err}
  <Popup message={err} href={"/admin/home"} text={"✕"} />
{/if}

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


