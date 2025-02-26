<script>
    import AnnouncementsList from "$lib/AnnouncementsList.svelte"
    import Loading from "$lib/Loading.svelte"
    import Popup from '$lib/Popup.svelte';

    let ctr = 6;
    
    async function fetchAnnouncements() {
        const res = await fetch(`https://trenph.up.railway.app/api/announcements/?format=json`);
        if (!res.ok) throw new Error("Failed to fetch announcements");
        return await res.json();
  }
</script>

<title>Announcements | Train Station Monitoring System</title>

{#await fetchAnnouncements()}
  <div class="flex-col items-center scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7 mx-20">
    <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
    <hr class="w-auto max-w-200 mx-auto h-30 bg-gray-200 border-0 rounded-sm dark:bg-gray-700 ">
    <Loading />
  </div>
{:then announcements}
  <div class="flex-col items-center scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7 mx-20">
    <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
    <hr class="w-auto max-w-200 mx-auto h-30 bg-gray-200 border-0 rounded-sm dark:bg-gray-700 ">
  </div>
  <br>
  <AnnouncementsList max={announcements.count} posts={announcements.results} />
{:catch error}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
      <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
    </div>
    <Popup message={error} href={"/admin/home"} text={"✕"} />
{/await}