<script>
  import AnnouncementsList from "$lib/AnnouncementsList.svelte"
  import Loading from "$lib/Loading.svelte"
  import Popup from '$lib/Popup.svelte';
  import Checkbox from "$lib/Checkbox3.svelte";
  import PostBox from '$lib/PostBox.svelte';
  import { browser } from '$app/environment';

  let username = '';
  if (browser) {
    username = localStorage.getItem("username") || "";
  }
  
  let subject = '';
  let body = '';
  let result = '';
  let tags = [];
  let filtered = [];
  $: filtered = filtered;

  let submitted = false;

  async function fetchAnnouncements() {
    const res = await fetch(`https://trenph.up.railway.app/api/announcements/?format=json`);
    if (!res.ok) throw new Error("Failed to fetch announcements");
    return await res.json();
  }

  async function postAnnouncement() {
    if(!submitted) {
      submitted = true;

      //const res = await fetch(`https://httpstat.us/500`);
      const res = await fetch('https://trenph.up.railway.app/api/announcements/create/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          author: username,
          subject: subject,
          body: body,
          tags: tags,
        })  
      });

      if (!res.ok) {
        result = 'Error! Unable to post announcement';
      }
      else {
        result = 'Announcement has been successfully posted!';
      } 
    }
  }
</script>

<title>Announcements | Train Station Monitoring System</title>

{#await fetchAnnouncements()}
  <div class="flex-col items-center scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7 mx-20">
    <div class="flex flex-col items-center justify-center inter-h1 text-3xl origin-top mt-6 space-y-2">
      <h1>Announcements</h1>
      <Checkbox disabled={true} />
    </div>
    <PostBox bind:subject={subject} bind:body={body} func={postAnnouncement} disabled={true}/>
    <Loading />
  </div>
{:then announcements}
  <div class="flex-col items-center scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7 mx-20">  
    <div class="flex flex-col items-center justify-center inter-h1 text-3xl origin-top mt-6 space-y-2">
      <h1>Announcements</h1>
      <Checkbox bind:selected={filtered}/>
    </div>
    <PostBox bind:subject={subject} bind:body={body} func={postAnnouncement} bind:tags={tags}/>
  </div>
  <br>
  <AnnouncementsList max={announcements.count} posts={announcements.results} filters={filtered} admin={1} />
      
  {#if result}
    {#if result.includes("Error!")}
      <Popup message={result} href={"/admin/home"} text={"✕"} />
    {:else}
      <Popup message={result} href={"/admin/announcements"} text={"✕"} color="bg-green-700" txtColor="text-green-700" />
    {/if}
  {/if}

{:catch error}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
      <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
    </div>
    <Popup message={"Error! No database connection"} href={"/admin/home"} text={"✕"} />
{/await}