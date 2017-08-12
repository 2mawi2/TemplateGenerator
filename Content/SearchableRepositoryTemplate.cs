using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using AutoMapper;
using Common;
using Common.Model.<#package#>;
using Microsoft.EntityFrameworkCore;
using Persistence;
using Persistence.<#package#>;
using Persistence.Filter;
using Persistence.Repositories;

namespace Persistence<#package#>.Repositories
{
    public class <#name#>Repository : SearchableRepository<<#name#>Entity, <#name#>,
            <#name#>.SortBy, <#name#>.FilterAttribute>,
        I<#name#>Repository
    {
        private readonly Lazy<WaWiContext> _context;
        protected override DbContext Context => _context.Value;

        public <#name#>Repository(Lazy<WaWiContext> context, IMapper mapper,
            ICurrentUser currentUser) : base(mapper, currentUser)
        {
            _context = context;
        }

        protected override SearchQuery<<#name#>Entity, <#name#>, <#name#>.SortBy,
            <#name#>.FilterAttribute> CreateSearchQuery()
        {
            return new <#name#>SearchQuery(Context, Mapper);
        }
    }

    public class <#name#>SearchQuery : SearchQuery<<#name#>Entity, <#name#>,
        <#name#>.SortBy, <#name#>.FilterAttribute>
    {
        public static readonly FilterDefinitionGroup<<#name#>Entity, <#name#>.FilterAttribute>
            FilterDefinitions =
                new FilterDefinitionGroup<<#name#>Entity, <#name#>.FilterAttribute>();

        static <#name#>SearchQuery()
        {
        }

        public <#name#>SearchQuery(DbContext context, IMapper mapper) : base(context, mapper)
        {
        }

        protected override void SortQuery(SortedQueryBuilder<<#name#>Entity> builder,
            <#name#>.SortBy sortBy)
        {
            switch (sortBy)
            {
                default:
                    MissingSortImplementation(sortBy);
                    break;
            }
        }

        protected override IFilterDefinition<<#name#>Entity> GetFilterDefinition(
            <#name#>.FilterAttribute attr)
        {
            return FilterDefinitions.GetFilterDefinition(attr);
        }
    }
}