<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;

class CrawlBlogSources extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'crawl:blog';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Crawl and collect blogs from external sources';

    /**
     * Execute the console command.
     */
    public function handle()
    {
        //
    }
}
