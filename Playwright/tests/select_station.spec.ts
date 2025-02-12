import { test, expect } from '@playwright/test';

test('working station - lrt1', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.locator('#train-lines').selectOption({label: 'LRT1'});
  await page.locator('#stations').selectOption({label: 'United Nations'});
  await page.getByRole('button').click();

  await expect(page).toHaveURL("https://trenph.vercel.app/stations?id=13");
});


test('working station - lrt2', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.locator('#train-lines').selectOption({label: 'LRT2'});
  await page.locator('#stations').selectOption({label: 'Katipunan'});
  await page.getByRole('button').click();

  await expect(page).toHaveURL("https://trenph.vercel.app/stations?id=30");
});


test('working station - mrt3', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.locator('#train-lines').selectOption({label: 'MRT3'});
  await page.locator('#stations').selectOption({label: 'Ortigas'});
  await page.getByRole('button').click();

  await expect(page).toHaveURL("https://trenph.vercel.app/stations?id=39");
});


test('non-operational station', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.locator('#train-lines').selectOption({label: 'LRT2'});
  await page.locator('#stations').selectOption({label: 'Recto'});
  await page.getByRole('button').click();

  await expect(page.getByText(/Error/)).toBeVisible;
});

