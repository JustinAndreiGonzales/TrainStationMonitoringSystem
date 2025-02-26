import { test, expect } from '@playwright/test';

test('home to stations, button', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/');

  await page.getByText('View station').click();

  await expect(page).toHaveURL("https://trenph.vercel.app/stations");
});

test('home to stations, navbar', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/');

  await page.getByText('Stations').click();

  await expect(page).toHaveURL("https://trenph.vercel.app/stations");
});

test('stations to home', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.getByText('Home').click();

  await expect(page).toHaveURL("https://trenph.vercel.app/");
});
