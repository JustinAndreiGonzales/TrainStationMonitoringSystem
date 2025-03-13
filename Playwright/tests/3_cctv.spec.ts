import { test, expect } from '@playwright/test';

test('CCTV - All Good', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations?id=2');

    //await page.getByPlaceholder('Title').fill('Some Title');

    await page.getByText('View CCTV').click()

    await expect(page).toHaveURL("https://trenph.vercel.app/stations/cctv?id=2&stream=1");

    await page.goto('https://trenph.vercel.app/stations?id=2');

    await page.getByTestId('current-density').getByText('Right').click();
    await page.getByText('View CCTV').click()

    await expect(page).toHaveURL("https://trenph.vercel.app/stations/cctv?id=2&stream=2");
  });

test('CCTV - L Good', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations?id=41');

    //await page.getByPlaceholder('Title').fill('Some Title');

    await page.getByText('View CCTV').click()

    await expect(page).toHaveURL("https://trenph.vercel.app/stations/cctv?id=41&stream=1");
  });

test('CCTV - R Good', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations?id=1');

    //await page.getByPlaceholder('Title').fill('Some Title');

    await page.getByTestId('current-density').getByText('Right').click();
    await page.getByText('View CCTV').click()

    await expect(page).toHaveURL("https://trenph.vercel.app/stations/cctv?id=1&stream=2");
  });

  test('CCTV - All Bad', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations?id=24');

    //await page.getByPlaceholder('Title').fill('Some Title');

    await expect(page.getByText('View CCTV')).toHaveCount(0);

    await page.getByTestId('current-density').getByText('Right').click();

    await expect(page.getByText('View CCTV')).toHaveCount(0);
  });