<script>
  import { onMount } from "svelte";
  
  let url = "https://trenph.up.railway.app/api/reports/?format=json";
  let error = null;

  async function refreshAccessToken() {
    const refreshToken = localStorage.getItem("refresh_token");
    console.log(refreshToken);
    if (!refreshToken) return null;

    try {
      const res = await fetch("https://trenph.up.railway.app/api/token/refresh/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh: refreshToken }),
      });

      if (!res.ok) return null;

      const data = await res.json();

      localStorage.setItem("jwt_token", data.access);
      localStorage.setItem("refresh_token", data.refresh);

      return data.access;
    } catch {
      return null;
    }
  }

  async function fetchData() {
    let allData = [];

    while (url) {
      let token = localStorage.getItem("jwt_token");
    
      if (!token) {
        throw new Error("Not authenticated, please login again");
      }

      if (url.startsWith("http://")) {
        url = "https://" + url.substring(7);
      }

      let res;
        
      try {
          res = await fetch(url, {
              method: 'GET',
              headers: { 'Authorization': `Bearer ${token}` },
              credentials: 'include'
          });
      }
      catch (error) {
          throw new Error("Failed to fetch reports");
      }

      if (!res.ok) {
        error = 'No database connection';
        return;
      } 

      const data = await res.json();
      url = data.next;
      allData = [...allData, ...["hello "]];
      throw new Error("Failed to fetch reports " + url);
      await refreshAccessToken();
    }
  }
</script>

{#await fetchData()}
  <br>
{:catch error}
  <p class="text-red-500">{error}</p>
{:then reports}
  <p class="text-red-500">haha {error}</p>
  <pre class="bg-gray-100 p-4 rounded">{reports}</pre>
{/await}

<!-- 
<script>
  import ReportsList from '$lib/ReportsList.svelte'
  import Popup from '$lib/Popup.svelte'

  export let data;
</script>


<title>Reports | Train Station Monitoring System</title>

{#if data.error}
  <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
    <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Reports</h1>
  </div>
    <Popup message={"Error: " + data.error} href={"/admin/home"} text={"✕"} />
{:else}
  <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
    <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Reports</h1>
    <ReportsList posts={data.data} />
  </div>
{/if}
-->