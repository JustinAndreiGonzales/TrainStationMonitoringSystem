<script>
  import GoToButton from "./GoToButton.svelte";
  import Popup from "./Popup.svelte";
  import PostBox from "./PostBox.svelte";

  export let id = "";
  export let posts = [];

  export let author = "";
  export let ogTitle = "";
  export let title = "";
  export let ogBody = "";
  export let body = "";
  export let selectedTags = [];
  let tags = [];
  let result = "";

  async function submitEdit()  {
    console.log("id is " + id);
    
    // [SP4] FIX: posts checking is stale
    if (posts.some(f => f.id === id)) {  
      const res = await fetch(`https://trenph.up.railway.app/api/announcements/update/${id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            id: id,
            author: author,
            subject: title,
            body: body,
            tags: tags,
          })  
      })

      if (!res.ok) {
        result = "Error! No database connection";
      }

      else {
        result = "Announcement has been successfully edited!"
      }    
    }

    else {
      result = "Error! Announcement could not be found."
    }
  }  
</script>

{#if result}
  {#if result.includes("Error!")}
    <Popup message={result} href={"/admin/announcements"} text={"✕"}/>
  {:else}
    <Popup message={result} href={"/admin/announcements"} text={"✕"} color="bg-green-700" txtColor="text-green-700"/>
  {/if}
{:else}
  <div class="fixed inset-0 backdrop-blur-[2px] z-40"></div>

  <div
    class="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-150 bg-gray-200 text-white text-lg rounded-lg shadow-lg p-8 z-50"
    role="alert"
  >
    <div class="flex flex-col items-center justify-center justify-between space-y-3 m-auto">
      <p class="flex text-left inter-h1 font-lg text-black">Edit Post</p>
      <div class="absolute top-5 right-8">
        
        <GoToButton href={"/admin/announcements"} text={"✕"} txtColor={"text-black"} bgColor={"bg-gray-200"} hvrColor={"hover:bg-red-500"} isBold={""}/>
      </div>

      <PostBox bind:subject={title} bind:body={body} func={submitEdit} disabled={false} bind:tags={tags} selectedTags={selectedTags} ogTitle={ogTitle} ogBody={ogBody} edit={true}/>
    </div>
  </div>
{/if}  

<style>
</style>
  