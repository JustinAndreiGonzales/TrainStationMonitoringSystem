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

    // REPLACE: maxAge (in sec)
    if (res.ok) {
        const data = await res.json();
        cookies.set('admin_auth', data.access, {
            path: '/admin',
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            maxAge: 60 * 10
        });

        cookies.set('refresh_token', data.refresh, {
            path: '/admin',
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            maxAge: 60 * 10
        });

        cookies.set('username', data.username, {
            path: '/admin',
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            maxAge: 60 * 10
        });

        cookies.set('role', data.role, {
            path: '/admin',
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            maxAge: 60 * 10
        });

        return json({ success: true, token: data.access, refresh: data.refresh, username: data.username, role: data.role });
    }

    return json({ success: false, message: 'Invalid credentials' }, { status: 401 });
}

export async function GET({ cookies }) {
    const token = cookies.get('admin_auth') || null;
    return new Response(JSON.stringify({ isLoggedIn: !!token }));
}

export async function DELETE({ cookies }) {
    cookies.delete('admin_auth', { path: '/admin' });
    cookies.delete('refresh_token', { path: '/admin' });
    cookies.delete('username', { path: '/admin' });
    cookies.delete('role', { path: '/admin' });
    return json({ success: true });
}