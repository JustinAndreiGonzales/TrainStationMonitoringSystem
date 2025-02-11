import { test, expect } from '@playwright/test';

test('working station', async ({ page }) => {
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

