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
    let matchingLink = currentLink();

    if (matchingLink && matchingLink.href === href) {
      event.preventDefault(); 
      window.location.href = href;
    }
  }

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
        <a href="{link.href}" 
        class="flex flex-col items-center text-white space-y-1"
        on:click={event => forceLink(link.href, event)}
        >
          <img src={link.img} alt={"icon.png"} class="w-5"/>
          <span class={textHighlight(link.href)}>{link.name}</span>
        </a>
      </li>
    {/each}
  </ul>
</footer>

<style>
</style>