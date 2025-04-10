<script>
  export let admin = 3;
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

  function deleteClick() {
    dispatch('deletePost', { id });
  }

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
        {#if admin % 3 == 1}
          <p class="inter-body text-gray-400 text-sm mt-[-5px]">Posted by: {author}</p>
        {/if}
      </div>
    </div>

    {#if admin % 3 == 1}
      <button aria-label="edit" class="flex flex-row space-x-2 justify-center max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 text-black inter-body text-sm w-full py-2 px-4 rounded mr-2" on:click={editClick}>
        <svg id="Layer_1" class="max-w-3" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 122.88 121.51"><title>edit</title><path d="M28.66,1.64H58.88L44.46,16.71H28.66a13.52,13.52,0,0,0-9.59,4l0,0a13.52,13.52,0,0,0-4,9.59v76.14H91.21a13.5,13.5,0,0,0,9.59-4l0,0a13.5,13.5,0,0,0,4-9.59V77.3l15.07-15.74V92.85a28.6,28.6,0,0,1-8.41,20.22l0,.05a28.58,28.58,0,0,1-20.2,8.39H11.5a11.47,11.47,0,0,1-8.1-3.37l0,0A11.52,11.52,0,0,1,0,110V30.3A28.58,28.58,0,0,1,8.41,10.09L8.46,10a28.58,28.58,0,0,1,20.2-8.4ZM73,76.47l-29.42,6,4.25-31.31L73,76.47ZM57.13,41.68,96.3.91A2.74,2.74,0,0,1,99.69.38l22.48,21.76a2.39,2.39,0,0,1-.19,3.57L82.28,67,57.13,41.68Z"/></svg>
        <p>Edit</p>
        <!--
        <button on:click={deleteClick} class="max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 text-black inter-body text-sm w-full py-2 px-4 rounded">Delete</button>
        -->
      </button>
    {/if}

    {#if admin % 3 == 2}
      <button aria-label="delete" class="flex flex-row space-x-2 justify-center max-w-sm mx-auto bg-gray-200 hover:bg-gray-300 text-black inter-body text-sm w-full py-2 px-4 rounded mr-2" on:click={deleteClick} >
        <svg id="Layer_1" class="max-w-3" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 110.61 122.88"><title>trash</title><path d="M39.27,58.64a4.74,4.74,0,1,1,9.47,0V93.72a4.74,4.74,0,1,1-9.47,0V58.64Zm63.6-19.86L98,103a22.29,22.29,0,0,1-6.33,14.1,19.41,19.41,0,0,1-13.88,5.78h-45a19.4,19.4,0,0,1-13.86-5.78l0,0A22.31,22.31,0,0,1,12.59,103L7.74,38.78H0V25c0-3.32,1.63-4.58,4.84-4.58H27.58V10.79A10.82,10.82,0,0,1,38.37,0H72.24A10.82,10.82,0,0,1,83,10.79v9.62h23.35a6.19,6.19,0,0,1,1,.06A3.86,3.86,0,0,1,110.59,24c0,.2,0,.38,0,.57V38.78Zm-9.5.17H17.24L22,102.3a12.82,12.82,0,0,0,3.57,8.1l0,0a10,10,0,0,0,7.19,3h45a10.06,10.06,0,0,0,7.19-3,12.8,12.8,0,0,0,3.59-8.1L93.37,39ZM71,20.41V12.05H39.64v8.36ZM61.87,58.64a4.74,4.74,0,1,1,9.47,0V93.72a4.74,4.74,0,1,1-9.47,0V58.64Z"/></svg>
        <p>Delete</p>
      </button>
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