import { test, expect, defineConfig } from '@playwright/test';

export default defineConfig({
  retries: 2,
})

//https://trenph.vercel.app/stations/report?id=2


test('report page accessible', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations/report?id=2');
  });

test('REPORT - double empty', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations/report?id=23');

    //await page.getByPlaceholder('Title').fill('Some Title');

    await page.getByRole('button').click()

    await page.getByText ("Report is incomplete and missing both fields.")

  });

test('REPORT - body empty', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations/report?id=3');

    await page.getByPlaceholder('Title').fill('Some Title');

    await page.getByRole('button').click()

    await page.getByText( "Report is incomplete and missing details")
  });

test('REPORT - title empty', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations/report?id=12');

    await page.getByPlaceholder('Write details here...').fill('Some Details');

    await page.getByRole('button').click()

    await page.getByText( "Report is incomplete and missing title.")
  });

test('REPORT - valid', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations/report?id=38');

    //let reference_number = Math.random()

    await page.getByPlaceholder('Title').fill(`Pyright Test`);
    await page.getByPlaceholder('Write details here...').fill('Some Details %s');

    await page.getByRole('button').click()

    // let url = 'https://trenph.vercel.app/admin';
    // let user = 'admin';
    // let pw = 'password';

    // await page.goto(url);

    // await page.getByPlaceholder('Username').fill(user);
    // await page.getByPlaceholder('Password').fill(pw);

    // await page.getByRole('button').click();

    // await page.getByText('Reports').click();

    // await page.getByText(`Test_ID: ${reference_number}`)
  });
