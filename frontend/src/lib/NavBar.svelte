<script>
  // Define your navigation links
  let links = [
    { name: "Home", href: "/" },
    { name: "Announcements", href: "/" },
    { name: "Stations", href: "/stations" },
    { name: "Routes", href: "/" }
  ];
</script>

<footer class="fixed bottom-0 w-full bg-blue-700 shadow-inner ">
  <ul class="flex justify-around list-none m-0 p-0">
    {#each links as link}
      <li class="flex flex-col items-center py-2">
        <a href="{link.href}" class="flex flex-col items-center text-white">
          <!-- FIX: add icons -->
          <div class="w-8 h-8 bg-gray-300 rounded-full mb-1"></div>
          <span class="text-xs">{link.name}</span>
        </a>
      </li>
    {/each}
  </ul>
</footer>
