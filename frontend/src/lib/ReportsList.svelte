<script>
  import Post from "$lib/Post.svelte";
  import { formatDateTime } from "./formatDateTime";

  export let current = 5;
  export let posts;
  export let filters = [];
  export let deleted = false;
  export let result = '';

  $: current = current;
  $: filteredPosts = filters.length ? posts.filter(post => post.station.split(',').some(tag => filters.includes(tag))) : posts;
  
  async function deletePost(id) {
    if (!deleted) {
      deleted = true;
      const token = localStorage.getItem('jwt_token');

      //const res = await fetch(`https://httpstat.us/500`);
      console.log(id);
      const res = await fetch(`https://trenph.up.railway.app/api/reports/delete/${id}/`, {
          method: 'DELETE',
          headers: { 'Authorization': `Bearer ${token}` },
        });

      if(!res.ok) {
        result = `Error! No database connnection`;
      }
      else {
        result = 'Report has been successfully deleted!'
      }
    }
  }
</script>


<div class="flex flex-col items-center min-h-screen space-y-7 pb-25">
  {#if !filteredPosts.length}
    <p class="text-sm inter-body">No available reports for selected filters.</p>
  {/if}
  {#each filteredPosts as p, i}
    {#if i > -1}
      {#if i > 0}
        <hr class="w-210 h-[0.5px] bg-gray-200 border-0">
      {/if}

      <Post 
        admin={2}
        id={p.id}
        tags={p.station.split(',')}
        subject={p.subject}
        body={p.body} 
        time={formatDateTime(p.datetimeReported).time} 
        date={formatDateTime(p.datetimeReported).date}
        on:deletePost={(e) => deletePost(e.detail.id)}
      />
    {/if}
  {/each}
</div>