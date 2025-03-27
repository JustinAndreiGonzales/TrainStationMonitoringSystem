import { test, expect } from '@playwright/test';

test('home page accessible', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/');

  await expect(page).toHaveTitle(/Train Station Monitoring System/);
});

test('stations page accessible', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await expect(page).toHaveTitle(/Stations/);
});
