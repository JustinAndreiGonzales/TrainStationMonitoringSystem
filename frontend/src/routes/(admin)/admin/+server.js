import { json } from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';

export async function POST({ request, cookies }) {
    const { username, password } = await request.json();

    const res = await fetch('https://trenph.up.railway.app/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
        credentials: 'include'
    });

    if (res.ok) {
        const data = await res.json();
        cookies.set('admin_auth', data.access, {
            path: '/admin',
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            // REPLACE: maxAge (in sec)
            maxAge: 60 * 5
        });

        return json({ success: true });
    }

    return json({ success: false, message: 'Invalid credentials' }, { status: 401 });
}

export async function GET({ cookies }) {
    const token = cookies.get('admin_auth') || null;
    return new Response(JSON.stringify({ isLoggedIn: !!token }));
}

export async function DELETE({ cookies }) {
    cookies.delete('admin_auth', { path: '/admin' });
    return json({ success: true });
}