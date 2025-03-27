import { test, expect } from '@playwright/test';

const url = 'https://trenph.vercel.app/admin';

test.beforeEach(async ({ page }) => {
  await page.goto(url);
});

test('open /home', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/admin/home');

  await expect(page).toHaveURL("https://trenph.vercel.app/admin");
});

test('open /reports', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/admin/reports');

  await expect(page).toHaveURL("https://trenph.vercel.app/admin");
});

test('open /announcements', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/admin/announcements');

  await expect(page).toHaveURL("https://trenph.vercel.app/admin");
});