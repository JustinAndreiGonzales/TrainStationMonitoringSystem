export async function load({ cookies }) {
    const token = cookies.get('admin_auth');
    console.log('---> TOKEN: ' + token);

    if (!token) {
        return { error: 'Not authenticated' };
    }

    let url = 'https://trenph.up.railway.app/api/reports/'
    let count = 0;
    let allData = [];

    try {
        while(url){
            // REMOVE !!
            const currToken = cookies.get('admin_auth');
            console.log(`---> [${count}]: ${url} `);
            console.log(`---> [${count}]: ${currToken} `);

            const res = await fetch(url, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${currToken}`
                },
                credentials: 'include'
            });

            // REMOVE !!            
            console.log(`---> [${count}]: ${res.ok} \n`);

            if (!res.ok) {    
                break;
            }
            
            const data = await res.json();
            url = data.next;
            allData = [...allData, ...data.results]

            // REMOVE !!
            count++;
        }
        
        if (allData.length != 0) {
            return { data: allData };
        }
        else {
            return { error: 'Failed to fetch data' };
        }
        
    } catch (err) {
        return { error: 'No database connection' };
    }
}
