<script>
  import { page } from "$app/stores";

  let links = [
    { name: "Home", href: "/", img: "/a.png" },
    { name: "Announcements", href: "/announcements", img: "/b.png" },
    { name: "Stations", href: "/stations", img: "/c.png" },
    { name: "Routes", href: "/routes", img: "/d.png" },  ];

  function currentLink() {
    return [...links].reverse().find(link => $page.url.pathname.startsWith(link.href)); 
  }

  function forceLink(href, event) {
    if ($page.url.pathname.startsWith("/stations")) {
      event.preventDefault();
      window.location.href = href;
    }
  }

  /* REPLACE ABOVE when Announcements/Routes are defined
  function forceLink(href, event) {
    let matchingLink = currentLink();

    if (matchingLink && matchingLink.href === href) {
      event.preventDefault(); 
      window.location.href = href;
    }
  }
  */
  
  function textHighlight(href) {
    let link = currentLink();
    
    if (link && link.href == href) {
      return "text-sm font-semibold inter-h1";   
    }
    return "text-xs inter-body";
  }
</script>

<footer class="fixed bottom-0 w-full bg-blue-700 shadow-inner ">
  <ul class="flex justify-around list-none m-0 p-0 mt-1">
    {#each links as link}
      <li class="flex flex-col items-center py-2">
        <!-- REMOVE if/else once Announcements/Routes are defined -->
        {#if link.name == 'Home' || link.name == 'Stations'}
          <a href="{link.href}" 
          class="flex flex-col items-center text-white space-y-1"
          on:click={event => forceLink(link.href, event)}
          >
            <img src={link.img} alt={"icon.png"} class="w-5"/>
            <span class={textHighlight(link.href)}>{link.name}</span>
          </a>
        {:else}
          <a href="{link.href}" 
          class="flex flex-col items-center text-white space-y-1 disable"
          on:click={event => forceLink(link.href, event)}
          >
            <img src={link.img} alt={"icon.png"} class="w-5"/>
            <span class={textHighlight(link.href)}>{link.name}</span>
          </a>
        {/if}
      </li>
    {/each}
  </ul>
</footer>

<!-- REMOVE once Announcements/Routes are defined -->
<style>
  a.disable {
    pointer-events: none;
  }
</style>