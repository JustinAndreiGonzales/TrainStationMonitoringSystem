async function refreshAccessToken(cookies) {
    const refreshToken = cookies.get('refresh_token');
    console.log('\n!! RAT1: ' + refreshToken);
    if (!refreshToken) return null;

    try {
        const res = await fetch('https://trenph.up.railway.app/api/token/refresh/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ refresh: refreshToken })
        });
        if (!res.ok) return null;

        const data = await res.json();
        cookies.set('admin_auth', data.access, {
            path: '/admin',
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            maxAge: 60 * 5
        });
        cookies.set('refresh_token', data.refresh, {
            path: '/admin',
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            maxAge: 60 * 5
        });

        console.log('\n!! RAT3: ' + data.access);
        return data.access;
    } catch (error) {
        return null;
    }
}

export async function load({ cookies }) {
    let token = cookies.get('admin_auth');
    if (!token) return { error: 'Not authenticated' };

    let url = 'https://trenph.up.railway.app/api/reports/?format=json';
    let allData = [];
    let counter = 0;

    while (url) {
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
            return { error: 'No database connection' };
        }
        if (!res.ok) break;

        const data = await res.json()
        console.log(data.next);
        url = data.next;
        allData = [...allData, ...data.results];

        const newToken = await refreshAccessToken(cookies);
        if (!newToken) break;
        token = newToken;
        counter++;
    }
        
    if(allData.length) {
        return { data: allData };
    }
    
    return { error: 'No database connection' };
}
