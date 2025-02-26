<script>
  export let title = "Title of post";
  export let pfpSrc = "";
  export let time = "12:51 PM";
  export let date = "31 Feb 1999";
  export let href = "";
  export let body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
  export let imgSrc = ""
  
  function navigate() {
    window.location.href = href;
  }
</script>

<div class="flex space-x-10 max-w-200">
  <div class="flex-row space-y-2">
    <div class="flex space-x-5">
      <!-- UPDATE TO IMG -->
      {#if pfpSrc}
        <p>{pfpSrc}</p>
      {/if}
      <div class="flex-row min-w-45 space-y-1">
        <p class="inter-h1 text-lg/6">{title}</p>
        <p class="inter-body text-gray-400 text-sm">{time} • {date}</p>
      </div>
    </div>

    <!-- INSERT BUTTON + EVENT -->
    {#if pfpSrc}
      <p>BUTTON</p>
    {/if}
  </div>

  <div class="flex-row inter-body space-y-2"> 
    <p class="text-md">{body}</p>
    {#if imgSrc}
      <!-- UPDATE TO IMG -->
      <p>{imgSrc}</p>
    {/if}
  </div>
</div>