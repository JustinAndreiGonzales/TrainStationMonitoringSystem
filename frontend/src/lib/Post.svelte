<script>
  export let admin = false;
  export let id = "";
  export let author = "";
  export let subject = "Title of post";
  export let pfpSrc = "";
  export let time = "12:51 PM";
  export let date = "31 Feb 1999";
  export let body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
  export let tags = [];
  export let imgSrc = ""

  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  
  function editClick() {
    dispatch('openPost', { id, author, subject, body, tags });
  }

  /* ADD: delete
  function deleteClick() {
    dispatch('deletePost', { id, subject, body });
  }
  */

</script>

<div class="flex space-x-10 max-w-200 portrait:flex-col space-y-3">
  <div class="flex-row space-y-2">
    {#if tags.length > 0}
      <div class="flex flex-row text-[10px] text-blue-500 inter-body space-x-2">
        {#each tags as t}
          <p class="outline-1 outline-blue-500 rounded-sm px-1.5 py-1">{t}</p>
        {/each}
      </div>
    {/if}
    
    <div class="flex space-x-5">
      <!-- UPDATE TO IMG -->
      {#if pfpSrc}
        <p>{pfpSrc}</p>
      {/if}

      <div class="flex-row min-w-45 space-y-1">
        <p class="inter-h1 text-lg/6">{subject}</p>
        <p class="inter-body text-gray-400 text-sm">{time} • {date}</p>
        {#if admin}
          <p class="inter-body text-gray-400 text-sm mt-[-5px]">Posted by: {author}</p>
        {/if}
      </div>
    </div>

    {#if admin}
      <div class="flex flex-row space-x-5">
        <button on:click={editClick} class="max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 text-black inter-body text-sm w-full py-2 px-4 rounded mr-2">Edit</button>
        <!--
        <button on:click={deleteClick} class="max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 text-black inter-body text-sm w-full py-2 px-4 rounded">Delete</button>
        -->
      </div>
    {/if}

    
  </div>

  <!-- UPDATE TO IMG min-w-145 -->
  <div class="flex-row inter-body space-y-2 min-w-75 sm:min-w-145"> 
    <p class="text-md">{body}</p>
    {#if imgSrc}
      <p>{imgSrc}</p>
    {/if}
  </div>
</div>

<style>
  @media (orientation: portrait) {
    .portrait\:flex-col {
      flex-direction: column;
    }
  }
</style>